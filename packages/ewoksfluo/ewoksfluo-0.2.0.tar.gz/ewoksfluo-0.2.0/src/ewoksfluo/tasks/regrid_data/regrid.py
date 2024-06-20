from typing import List, Dict, Callable, Sequence, Tuple

import h5py
import numpy
from ewokscore import Task

from . import utils
from .. import nexus
from ..utils import get_nxdata_groups


class RegridOnCoordinates(
    Task,
    input_names=["scan_uri", "fit_results_uri", "output_uri"],
    optional_input_names=[
        "positioners",
        "positioner_uri_template",
        "interpolate",
        "flatten",
    ],
    output_names=["regridded_uri"],
):
    """Regrid data on a regular grid by interpolation or reshaping."""

    def run(self):
        start_time = nexus.now()
        scan_uri: str = self.inputs.scan_uri
        fit_results_uri: str = self.inputs.fit_results_uri
        output_uri: str = self.inputs.output_uri
        position_suburis = self._get_position_suburis(scan_uri)
        interpolate: str = self.get_input_value("interpolate", "linear")
        if interpolate == "none":
            interpolate = None

        if interpolate:
            # NXdata groups will be regular grid plots
            grid = utils.ScanGrid(method=interpolate)
            interpolator = grid.get_interpolator(scan_uri, position_suburis)
            scan_size = grid.meshgrid_coordinates[0].size
        else:
            # NXdata groups will be scatter plots
            flatten: bool = self.get_input_value("flatten", True)
            positions, names = utils.scan_scatter_coordinates_from_uris(
                scan_uri, position_suburis
            )
            if flatten:
                # Option exists because not all NXdata viewers can properly
                # handle scatter data.
                positions = [data.flatten() for data in positions]
            scan_shape = positions[0].shape
            scan_size = positions[0].size

        fit_results_filename, fit_results_h5path = nexus.split_h5uri(fit_results_uri)

        with nexus.save_in_ewoks_subprocess(
            output_uri, start_time, {}, default_levels=("results", "regrid")
        ) as regrid_results:
            with h5py.File(fit_results_filename, "r") as fit_results_file:
                fit_results_grp = fit_results_file[fit_results_h5path]
                if not isinstance(fit_results_grp, h5py.Group):
                    raise TypeError(f"'{fit_results_uri}' must be a group")

                nxdata_groups = get_nxdata_groups(fit_results_grp)

                for group_name in reversed(list(nxdata_groups)):
                    input_grp = fit_results_grp[group_name]
                    input_datasets = {
                        dset_name: dset
                        for dset_name, dset in input_grp.items()
                        if isinstance(dset, h5py.Dataset) and dset.size == scan_size
                    }
                    if not input_datasets:
                        # NXdata group which does not plot scan data
                        continue

                    # NXdata signals
                    output_grp = nexus.create_data(regrid_results, group_name)
                    if interpolate:
                        self._save_grid_data(input_datasets, interpolator, output_grp)
                    else:
                        self._save_scatter_data(input_datasets, scan_shape, output_grp)
                    nexus.set_data_signals(
                        output_grp, signals=tuple(input_datasets.keys())
                    )

                    # NXdata axes
                    if interpolate:
                        self._save_grid_axes(grid, output_grp)
                    elif flatten:
                        self._save_flat_scatter_axes(positions, names, output_grp)
                    else:
                        self._save_scatter_axes(positions, names, output_grp)

        self.outputs.regridded_uri = f"{output_uri}/regrid"

    def _get_position_suburis(self, scan_uri: str) -> List[str]:
        positioners = self.get_input_value("positioners", None)
        if not positioners:
            return utils.get_scan_position_suburis(scan_uri)
        if isinstance(positioners, str):
            positioners = [positioners]
        template = self.get_input_value("positioner_uri_template", "measurement/{}")
        return [template.format(s) for s in positioners]

    def _save_scatter_axes(
        self,
        positions: Sequence[numpy.ndarray],
        names: Sequence[str],
        output_grp: h5py.Group,
    ) -> None:
        axes = list()  # Order: slow to fast axis
        spanned = list(range(len(positions)))
        for axisname, arr in zip(names, positions):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
            output_grp.create_dataset(f"{axisname}_indices", data=spanned)
        output_grp.attrs["axes"] = axes  # Order: not relevant

    def _save_flat_scatter_axes(
        self,
        positions: Sequence[numpy.ndarray],
        names: Sequence[str],
        output_grp: h5py.Group,
    ) -> None:
        axes = list()  # Order: slow to fast axis
        for axisname, arr in zip(names, positions):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
        output_grp.attrs["axes"] = axes[::-1]  # Order: fast to slow axis

    def _save_grid_axes(self, grid: utils.ScanGrid, output_grp: h5py.Group) -> None:
        axes = list()  # Order: slow to fast axis
        for i, (axisname, arr) in enumerate(zip(grid.names, grid.mesh_coordinates)):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
            output_grp.create_dataset(f"{axisname}_indices", data=i)
        output_grp.attrs["axes"] = axes  # Order: not relevant

    def _save_grid_data(
        self,
        input_datasets: Dict[str, h5py.Dataset],
        interpolator: Callable[[numpy.ndarray], numpy.ndarray],
        output_grp: h5py.Group,
    ) -> None:
        for dset_name, dset in input_datasets.items():
            output_grp.create_dataset(dset_name, data=interpolator(dset[()]))

    def _save_scatter_data(
        self,
        input_datasets: Dict[str, h5py.Dataset],
        scan_shape: Tuple[int],
        output_grp: h5py.Group,
    ) -> None:
        for dset_name, dset in input_datasets.items():
            utils.save_dataset_link(
                dset, output_grp, dset_name, destination_shape=scan_shape
            )
