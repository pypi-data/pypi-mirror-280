from typing import Sequence, Optional

import h5py

from .nexus import split_h5uri

_ENERGY_UNITS = "kev", "ev"
_ENERGY_TEMPLATE = "instrument/positioners_start/{}"


def get_energy_suburi(scan_uri: str) -> Optional[str]:
    return _get_unit_position_suburi(scan_uri, _ENERGY_UNITS)


def get_energy(
    scan_uri: str,
    energy_name: Optional[str] = None,
    energy_uri_template: Optional[str] = None,
) -> Optional[float]:
    if energy_name:
        if not energy_uri_template:
            energy_uri_template = _ENERGY_TEMPLATE
        return _get_template_position_value(scan_uri, energy_name, energy_uri_template)
    return _get_unit_position_value(scan_uri, _ENERGY_UNITS)


def _get_unit_position_suburi(scan_uri: str, units: Sequence[str]) -> Optional[str]:
    """Get scan sub-URI for a positioner with specific units"""
    scan_filename, scan_h5path = split_h5uri(scan_uri)

    with h5py.File(scan_filename, "r") as nxroot:
        positioners = nxroot[f"{scan_h5path}/instrument/positioners_start"]
        name = _get_positioner_name(positioners, units)
        if name is not None:
            return f"instrument/positioners_start/{name}"


def _get_template_position_value(
    scan_uri: str, position_name: str, position_uri_template: str
) -> float:
    """Get position value from scan"""
    scan_filename, scan_h5path = split_h5uri(scan_uri)
    suburi = position_uri_template.format(position_name)
    with h5py.File(scan_filename, "r") as nxroot:
        return nxroot[f"{scan_h5path}/{suburi}"][()]


def _get_unit_position_value(scan_uri: str, units: Sequence[str]) -> Optional[float]:
    """Get position value from scan"""
    scan_filename, scan_h5path = split_h5uri(scan_uri)
    with h5py.File(scan_filename, "r") as nxroot:
        positioners = nxroot[f"{scan_h5path}/instrument/positioners_start"]
        positioner = _get_positioner(positioners, units)
        if positioner is not None:
            return positioner[()]


def _get_positioner(
    positioners: h5py.Group, units: Sequence[str]
) -> Optional[h5py.Dataset]:
    for name in positioners:
        positioner = positioners[name]
        punits = positioner.attrs.get("units", "").lower()
        if punits in units:
            return positioner


def _get_positioner_name(
    positioners: h5py.Group, units: Sequence[str]
) -> Optional[str]:
    for name in positioners:
        positioner = positioners[name]
        punits = positioner.attrs.get("units", "").lower()
        if punits in units:
            return name
