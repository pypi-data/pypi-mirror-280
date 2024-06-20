from typing import Sequence

import numpy
import h5py
from ewokscore import Task

from . import nexus
from .utils import get_correction_factor
from .positioner_utils import get_energy


DEFAULTS = {
    "xrf_spectra_uri_template": "instrument/{}/data",
    "livetime_uri_template": "instrument/{}/live_time",
    "livetime_reference_value": 1,
    "energy_name": None,
    "energy_uri_template": "instrument/positioners_start/{}",
}


class SumDetectors(
    Task,
    input_names=[
        "scan_uri",
        "detector_names",
        "output_uri",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "energy_name",
        "energy_uri_template",
        "livetime_uri_template",
        "livetime_reference_value",
    ],
    output_names=[
        "scan_uri",
        "detector_name",
        "xrf_spectra_uri_template",
    ],
):
    def run(self):
        start_time = nexus.now()
        params = {**DEFAULTS, **self.get_input_values()}

        scan_uri: str = params["scan_uri"]
        detector_names: Sequence[str] = params["detector_names"]
        xrf_spectra_uri_template: str = params["xrf_spectra_uri_template"]
        energy_name: str = params["energy_name"]
        energy_uri_template: str = params["energy_uri_template"]
        livetime_uri_template: str = params["livetime_uri_template"]
        livetime_reference_value: float = params["livetime_reference_value"]
        output_uri: str = params["output_uri"]

        if len(detector_names) < 1:
            raise ValueError("Expected at least 1 detector to sum")

        input_file, scan_h5path = nexus.split_h5uri(scan_uri)

        with h5py.File(input_file, "r") as h5file:
            summed_data = None
            scan_group = h5file[scan_h5path]

            energy = get_energy(scan_uri, energy_name, energy_uri_template)

            for detector_name in detector_names:
                xrf_spectra_dataset = scan_group[
                    xrf_spectra_uri_template.format(detector_name)
                ]
                assert isinstance(xrf_spectra_dataset, h5py.Dataset)
                xrf_spectra_data = xrf_spectra_dataset[()]

                livetime_uri = (
                    f"{scan_uri}/{livetime_uri_template.format(detector_name)}"
                )
                correction = get_correction_factor(
                    [livetime_uri], [livetime_reference_value]
                )

                if summed_data is None:
                    summed_data = numpy.zeros_like(
                        xrf_spectra_data, dtype="float32"
                    )  # Cast to float since the correction is a floating-point division

                summed_data += xrf_spectra_data * correction.reshape(
                    (len(correction), 1)
                )

        with nexus.save_in_ewoks_process(
            output_uri,
            start_time,
            process_config={"livetime_reference_value": livetime_reference_value},
            default_levels=("results", "sumdetectors"),
        ) as process_group:
            results_group = nexus.create_data(process_group, "mcasum", signal="data")
            results_group.create_dataset("data", data=summed_data)
            if energy is not None:
                dset = process_group.create_dataset(
                    "instrument/positioners_start/energy", data=energy
                )
                dset.attrs["units"] = "keV"
                process_group["instrument"].attrs["NX_class"] = "NXinstrument"
                process_group["instrument/positioners_start"].attrs[
                    "NX_class"
                ] = "NXcollection"

            self.outputs.scan_uri = (
                f"{process_group.file.filename}::{process_group.name}"
            )
        self.outputs.detector_name = "mcasum"
        self.outputs.xrf_spectra_uri_template = "{}/data"
