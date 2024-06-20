from typing import Sequence

from ewokscore import Task

from .. import nexus
from .utils import compute_summed_fractions, compute_summed_parameters, save_summed_dict

DEFAULTS = {
    "livetime_uri_template": "instrument/{}/live_time",
    "livetime_reference_value": 1,
}


class SumFitResults(
    Task,
    input_names=[
        "fit_results_uris",
        "scan_uri",
        "output_uri",
    ],
    optional_input_names=["livetime_uri_template", "livetime_reference_value"],
    output_names=["summed_results_uri"],
):
    """Add fit results of multiple detectors"""

    def run(self) -> None:
        start_time = nexus.now()
        params = {**DEFAULTS, **self.get_input_values()}

        fit_results_uris: Sequence[str] = params["fit_results_uris"]
        scan_uri: str = params["scan_uri"]
        livetime_uri_template: str = params["livetime_uri_template"]
        livetime_reference_value: float = params["livetime_reference_value"]
        output_uri: str = params["output_uri"]

        # Result URI's are expected to look like this
        # processed_data.h5::/results/fit/<detector_name>/results
        detector_names = [
            [s for s in uri.split("/") if s][-2] for uri in fit_results_uris
        ]
        livetime_uris = [
            f"{scan_uri}/{livetime_uri_template.format(name)}"
            for name in detector_names
        ]

        (
            summed_parameters,
            summed_uncertainties,
            has_massfractions,
        ) = compute_summed_parameters(
            fit_results_uris, livetime_uris, livetime_reference_value
        )

        if has_massfractions:
            summed_fractions = compute_summed_fractions(
                fit_results_uris,
                livetime_uris,
                livetime_reference_value,
                summed_parameters,
            )
        else:
            summed_fractions = None

        with nexus.save_in_ewoks_process(
            output_uri,
            start_time,
            process_config={"livetime_reference_value": livetime_reference_value},
            default_levels=("results", "sumfit"),
        ) as process_group:
            results_group = process_group.create_group("results")
            results_group.attrs["NX_class"] = "NXcollection"

            param_group = save_summed_dict(
                results_group, "parameters", summed_parameters
            )
            error_group = save_summed_dict(
                results_group, "uncertainties", summed_uncertainties
            )
            # Add `errors` links
            for name in param_group:
                param_group[f"{name}_errors"] = error_group[name]

            if summed_fractions is not None:
                save_summed_dict(results_group, "massfractions", summed_fractions)

            self.outputs.summed_results_uri = (
                f"{results_group.file.filename}::{results_group.name}"
            )
