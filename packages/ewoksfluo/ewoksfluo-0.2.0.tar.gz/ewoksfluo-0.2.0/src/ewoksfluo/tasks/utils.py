from typing import Dict, Sequence, Union

import h5py
import numpy

from .nexus import split_h5uri


def get_time_in_seconds(time_dset: h5py.Dataset) -> numpy.ndarray:
    unit = time_dset.attrs.get("units", "s")

    if unit == "ms":
        return time_dset[()] / 1000

    if unit == "s":
        return time_dset[()]

    raise ValueError(f"Unknown unit {unit} in {time_dset.name}")


def get_correction_factor(
    normalize_uris: Sequence[str], normalize_reference_values: Sequence[float]
) -> Union[float, numpy.ndarray]:
    """
    Get correction factor by resolving normalize_uris:

        reference_1 / normalize_1 * ... reference_N / normalize_N
    """
    if not normalize_reference_values:
        normalize_reference_values = [1] / len(normalize_uris)
    elif len(normalize_uris) != len(normalize_reference_values):
        raise ValueError(
            "Monitor and reference lists should have the same number of elements!"
        )

    correction_factor = 1.0
    for normalize_uri, reference in zip(normalize_uris, normalize_reference_values):
        normalize_file, normalize_h5path = split_h5uri(normalize_uri)

        with h5py.File(normalize_file, "r") as h5file:
            normalize_dset = h5file[normalize_h5path]
            assert isinstance(normalize_dset, h5py.Dataset)
            correction_factor = correction_factor * reference / normalize_dset[()]

    return correction_factor


def get_nxdata_groups(parent_nxdata: h5py.Group) -> Dict[str, h5py.Group]:
    """Most important group comes first"""
    groups = {
        k: v
        for k, v in parent_nxdata.items()
        if isinstance(v, h5py.Group) and v.attrs.get("NX_class") == "NXdata"
    }

    groups = {
        k: v
        for k, v in sorted(
            groups.items(),
            key=lambda tpl: (
                _NXDATA_ORDER.index(tpl[0])
                if tpl[0] in _NXDATA_ORDER
                else len(_NXDATA_ORDER)
            ),
        )
    }

    if len(groups) == 0:
        raise ValueError(f"No NXdata groups in {parent_nxdata.name}!")

    return groups


_NXDATA_ORDER = [
    "fit",
    "derivatives",
    "massfractions",
    "parameters",
    "uncertainties",
    "diagnostics",
]
