from ewokscore import Task

from .execute import fit_single
from .execute import fit_multi
from ..positioner_utils import get_energy


DEFAULTS = {
    "xrf_spectra_uri_template": "instrument/{}/data",
    "energy_uri_template": "instrument/positioners_start/{}",
    "fast_fitting": True,
    "diagnostics": False,
}


class FitSingleScanSingleDetector(
    Task,
    input_names=[
        "scan_uri",
        "detector_name",
        "config",
        "output_uri_template",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "energy_name",
        "energy_uri_template",
        "quantification",
        "energy_multiplier",
        "fast_fitting",
        "diagnostics",
        "figuresofmerit",
    ],
    output_names=["fit_results_uri"],
):
    """XRF fit of one scan with one detector"""

    def run(self):
        params = {**DEFAULTS, **self.get_input_values()}
        _parse_energy(params)
        fit_results_uri = fit_single(**params)
        self.outputs.fit_results_uri = fit_results_uri


class FitSingleScanMultiDetector(
    Task,
    input_names=[
        "scan_uri",
        "detector_names",
        "configs",
        "output_uri_template",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "energy_name",
        "energy_uri_template",
        "quantification",
        "energy_multiplier",
        "fast_fitting",
        "diagnostics",
        "figuresofmerit",
    ],
    output_names=["fit_results_uris"],
):
    """XRF fit of one scan with multiple detectors"""

    def run(self):
        params = {**DEFAULTS, **self.get_input_values()}
        params["scan_uris"] = [params.pop("scan_uri")]
        _parse_energies(params)
        fit_results_uris = fit_multi(**params)
        self.outputs.fit_results_uris = fit_results_uris


class FitMultiScanSingleDetector(
    Task,
    input_names=[
        "scan_uris",
        "detector_name",
        "config",
        "output_uri_template",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "energy_name",
        "energy_uri_template",
        "quantification",
        "energy_multiplier",
        "fast_fitting",
        "diagnostics",
        "figuresofmerit",
    ],
    output_names=["fit_results_uri"],
):
    """XRF fit of multiple scans with one detector"""

    def run(self):
        params = {**DEFAULTS, **self.get_input_values()}
        params["detector_names"] = [params.pop("detector_name")]
        params["configs"] = [params.pop("config")]
        _parse_energies(params)
        fit_results_uris = fit_multi(**params)
        self.outputs.fit_results_uri = fit_results_uris[0]


class FitMultiScanMultiDetector(
    Task,
    input_names=[
        "scan_uris",
        "detector_names",
        "configs",
        "output_uri_template",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "energy_name",
        "energy_uri_template",
        "quantification",
        "energy_multiplier",
        "fast_fitting",
        "diagnostics",
        "figuresofmerit",
    ],
    output_names=["fit_results_uris"],
):
    """XRF fit of multiple scans with multiple detectors"""

    def run(self):
        params = {**DEFAULTS, **self.get_input_values()}
        _parse_energies(params)
        fit_results_uris = fit_multi(**params)
        self.outputs.fit_results_uris = fit_results_uris


def _parse_energy(params: dict) -> None:
    energy_name = params.pop("energy_name", None)
    energy_uri_template = params.pop("energy_uri_template", None)
    params["energy"] = get_energy(params["scan_uri"], energy_name, energy_uri_template)


def _parse_energies(params: dict) -> None:
    energy_name = params.pop("energy_name", None)
    energy_uri_template = params.pop("energy_uri_template", None)
    params["energies"] = [
        get_energy(scan_uri, energy_name, energy_uri_template)
        for scan_uri in params["scan_uris"]
    ]
