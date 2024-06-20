import re
from typing import Dict, Sequence

import h5py
import numpy

from .. import nexus
from ..utils import get_correction_factor


def compute_summed_parameters(
    fit_results_uris: Sequence[str],
    livetime_uris: Sequence[str],
    livetime_reference_value: float,
):
    summed_parameters = {}
    summed_squared_uncertainties = {}
    has_massfractions = False

    for (
        fit_results_uri,
        livetime_uri,
    ) in zip(fit_results_uris, livetime_uris):
        fit_filename, fit_h5path = fit_results_uri.split("::")

        correction = get_correction_factor([livetime_uri], [livetime_reference_value])

        with h5py.File(fit_filename, "r") as h5file:
            fit_results_group = h5file[fit_h5path]
            assert isinstance(fit_results_group, h5py.Group)
            has_massfractions = "massfractions" in fit_results_group

            param_group = fit_results_group["parameters"]
            assert isinstance(param_group, h5py.Group)

            for dset_name, dset in param_group.items():
                if not isinstance(dset, h5py.Dataset) or dset_name.endswith("errors"):
                    continue

                if dset_name not in summed_parameters:
                    summed_parameters[dset_name] = dset[()] * correction
                else:
                    summed_parameters[dset_name] += dset[()] * correction

            uncertainties_group = fit_results_group["uncertainties"]
            assert isinstance(uncertainties_group, h5py.Group)

            for dset_name, dset in uncertainties_group.items():
                if not isinstance(dset, h5py.Dataset):
                    continue

                if dset_name not in summed_squared_uncertainties:
                    summed_squared_uncertainties[dset_name] = dset[()] * correction**2
                else:
                    summed_squared_uncertainties[dset_name] += dset[()] * correction**2

    summed_uncertainties = {
        k: numpy.sqrt(v) for k, v in summed_squared_uncertainties.items()
    }

    return summed_parameters, summed_uncertainties, has_massfractions


def compute_summed_fractions(
    fit_results_uris: Sequence[str],
    livetime_uris: Sequence[str],
    livetime_reference_value: float,
    summed_parameters: dict,
):
    element_parameters = {
        k: v for k, v in summed_parameters.items() if is_element_name(k)
    }
    total_sum = sum(element_parameters.values())
    weights = {k: v / total_sum for k, v in element_parameters.items()}

    result = {}

    for fit_results_uri, livetime_uri in zip(fit_results_uris, livetime_uris):
        fit_filename, fit_h5path = fit_results_uri.split("::")

        correction = get_correction_factor([livetime_uri], [livetime_reference_value])

        with h5py.File(fit_filename, "r") as h5file:
            fit_results_group = h5file[fit_h5path]
            assert isinstance(fit_results_group, h5py.Group)

            fit_results_group = h5file[fit_h5path]
            assert isinstance(fit_results_group, h5py.Group)
            massfractions_group = fit_results_group["massfractions"]
            assert isinstance(massfractions_group, h5py.Group)

            for dset_name, dset in massfractions_group.items():
                if not isinstance(dset, h5py.Dataset):
                    continue

                if dset_name not in result:
                    result[dset_name] = dset[()] * weights[dset_name] * correction
                else:
                    result[dset_name] += dset[()] * weights[dset_name] * correction

    return result


ELEMENT_REGEXP = re.compile(r"[a-zA-Z]+_[KLM][a-b1-5]?")


def is_element_name(dset_name: str) -> bool:
    """Checks if a dataset name refers to an element. Element names are of the form `[Element]-[Line]`
    Ex: Si-K, C-L, Fe-M.
    """
    return ELEMENT_REGEXP.match(dset_name) is not None


def save_summed_dict(
    parent: h5py.Group, name: str, summed_dict: Dict[str, numpy.ndarray]
):
    nxgroup = nexus.create_data(parent, name)

    default = None
    for name, data in summed_dict.items():
        if default is None:
            default = name
        nxgroup.create_dataset(name, data=data)

    nxgroup.attrs["default"] = default

    return nxgroup
