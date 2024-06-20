from typing import Sequence
from ewokscore import Task
import h5py

from .utils import get_correction_factor
from .utils import get_nxdata_groups
from . import nexus


class Normalization(
    Task,
    input_names=[
        "data_uri",
        "normalize_uris",
        "output_uri",
    ],
    optional_input_names=["normalize_reference_values"],
    output_names=["corr_data_uri"],
):
    """
    Normalize data given a list of normalizers and references:
        data * reference_1 / normalize_1 * ... * reference_N / normalize_N

    Typical normalizers are beam monitors and measurement (live) time.

    :param data: URI to the group containing the data to be corrected. Format: /path/to/file.h5::/path/to/results/group.
    :param normalize_uris: URIs to the datasets to normalize the data to. Format: /path/to/file.h5::/path/to/normalizer/dataset.
    :param normalize_reference_values: List of reference values for each normalizer dataset.
    :param output_uri: URI to the nexusprocess where the results must be saved. Format: /path/to/file.h5::/entry/process
    :returns corr_data_uri: URI to the nexuscollection where the results were saved.
    """

    def run(self):
        start_time = nexus.now()
        output_uri = self.inputs.output_uri
        data_uri = self.inputs.data_uri
        normalize_uris: Sequence[str] = self.inputs.normalize_uris
        if isinstance(normalize_uris, str):
            normalize_uris = [normalize_uris]
        normalize_reference_values: Sequence[float] = self.get_input_value(
            "normalize_reference_values", list()
        )
        if not isinstance(normalize_reference_values, Sequence):
            if normalize_reference_values is None:
                normalize_reference_values = list()
            else:
                normalize_reference_values = [normalize_reference_values]
        correction = get_correction_factor(normalize_uris, normalize_reference_values)

        data_file, data_h5path = nexus.split_h5uri(data_uri)
        output_file, _ = nexus.split_h5uri(output_uri)

        with h5py.File(data_file, "r" if data_file != output_file else "a") as h5file:
            fit_results_group = h5file[data_h5path]
            assert isinstance(fit_results_group, h5py.Group)

            group_to_corr = get_nxdata_groups(fit_results_group)

            with nexus.save_in_ewoks_subprocess(
                output_uri,
                start_time,
                process_config={
                    "normalize_reference_values": normalize_reference_values
                },
                default_levels=("results", "normalized"),
            ) as results_group:
                results_group.attrs["default"] = tuple(group_to_corr.keys())[0]

                for group_name in reversed(list(group_to_corr)):
                    group = group_to_corr[group_name]
                    corr_group = nexus.create_data(results_group, group_name)

                    for dset_name, dset in group.items():
                        link = group.get(dset_name, getlink=True)
                        if not isinstance(link, h5py.HardLink) or not isinstance(
                            dset, h5py.Dataset
                        ):
                            continue
                        corr_group.create_dataset(dset_name, data=dset[()] * correction)
                        if "signal" not in corr_group.attrs:
                            corr_group.attrs["signal"] = dset_name

        self.outputs.corr_data_uri = f"{output_uri}/results"
