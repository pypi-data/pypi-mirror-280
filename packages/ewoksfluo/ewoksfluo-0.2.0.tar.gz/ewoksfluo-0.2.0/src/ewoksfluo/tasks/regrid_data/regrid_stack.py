from typing import Sequence, List

import h5py
from ewokscore import Task

from . import utils
from .. import nexus
from ..utils import get_nxdata_groups
from ..positioner_utils import get_energy_suburi


class RegridStackOnCoordinates(
    Task,
    input_names=["scan_uris", "fit_results_uri", "output_uri"],
    optional_input_names=[
        "stack_positioner",
        "positioners",
        "positioner_uri_template",
        "interpolate",
    ],
    output_names=["regridded_uri"],
):
    def run(self):
        start_time = nexus.now()
        scan_uris: Sequence[str] = self.inputs.scan_uris
        fit_results_uri: str = self.inputs.fit_results_uri
        output_uri: str = self.inputs.output_uri
        position_suburis = self._get_position_suburis(scan_uris)
        stack_suburi = self._get_stack_suburi(scan_uris, position_suburis)
        interpolate: str = self.get_input_value("interpolate", "linear")

        grid = utils.ScanGrid(method=interpolate)

        fit_results_filename, fit_results_h5path = nexus.split_h5uri(fit_results_uri)

        with nexus.save_in_ewoks_subprocess(
            output_uri, start_time, {}, default_levels=("results", "regrid")
        ) as regrid_results:
            with h5py.File(fit_results_filename, "r") as fit_results_file:
                fit_results_grp = fit_results_file[fit_results_h5path]
                if not isinstance(fit_results_grp, h5py.Group):
                    raise TypeError(f"'{fit_results_h5path}' must be a group")

                nxdata_groups = get_nxdata_groups(fit_results_grp)

                # Get fit result datasets (inputs) and output dataset information
                input_datasets = list()
                output_info = list()
                output_grps = list()
                for group_name in reversed(list(nxdata_groups)):
                    input_grp = fit_results_grp[group_name]

                    output_grp = nexus.create_data(regrid_results, group_name)
                    output_grps.append(output_grp)

                    signals = list()
                    for dset_name, dset in input_grp.items():
                        if not isinstance(dset, h5py.Dataset):
                            continue
                        key = group_name, dset_name
                        input_datasets.append(dset)
                        output_info.append((output_grp, group_name, dset_name))
                        signals.append(dset_name)

                    nexus.set_data_signals(output_grp, signals=signals)

                # NXdata signals
                nscans = len(scan_uris)
                output_datasets = dict()
                stack_axis = list()
                for scan_index, (scan_uri, *input_data) in enumerate(
                    zip(scan_uris, *input_datasets)
                ):
                    stack_axis.append(utils.get_position_data(scan_uri, stack_suburi))
                    interpolator = grid.get_interpolator(scan_uri, position_suburis)
                    for (output_grp, group_name, dset_name), data in zip(
                        output_info, input_data
                    ):
                        data = interpolator(data)
                        key = group_name, dset_name
                        dset = output_datasets.get(key)
                        if dset is None:
                            stack_shape = (nscans,) + data.shape
                            dset = output_grp.create_dataset(
                                dset_name, shape=stack_shape, dtype=data.dtype
                            )
                            output_datasets[key] = dset
                        dset[scan_index] = data

                # NXdata axes
                axes_data = [stack_axis] + grid.mesh_coordinates
                axes_names = (
                    stack_suburi.split("/")[-1],
                ) + grid.names  # Order: slow to fast axis
                for output_grp in output_grps:
                    for i, (axisname, arr) in enumerate(zip(axes_names, axes_data)):
                        output_grp.create_dataset(axisname, data=arr)
                        output_grp.create_dataset(f"{axisname}_indices", data=i)
                    output_grp.attrs["axes"] = axes_names  # Order: not relevant

        self.outputs.regridded_uri = f"{output_uri}/results"

    def _get_position_suburis(self, scan_uris: Sequence[str]) -> List[str]:
        positioners = self.get_input_value("positioners", None)
        if positioners:
            if isinstance(positioners, str):
                positioners = [positioners]
            template = self._get_positioner_uri_template()
            return [template.format(s) for s in positioners]
        return utils.get_scan_position_suburis(scan_uris[0])

    def _get_stack_suburi(
        self, scan_uris: Sequence[str], position_suburis: List[str]
    ) -> str:
        stack_positioner = self.get_input_value("stack_positioner", None)
        if stack_positioner:
            template = self._get_positioner_uri_template()
            return template.format(stack_positioner)
        return get_energy_suburi(scan_uris[0])

    def _get_positioner_uri_template(self) -> str:
        return self.get_input_value("positioner_uri_template", "measurement/{}")
