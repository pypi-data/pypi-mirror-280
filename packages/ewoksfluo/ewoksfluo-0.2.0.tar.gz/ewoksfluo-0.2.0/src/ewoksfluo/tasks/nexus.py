import json
import logging
import contextlib
from datetime import datetime
from typing import Any, Dict, Optional, Sequence, Union, Tuple, Generator

import numpy
import h5py
from silx.io.url import DataUrl
from ewoksdata.data import nexus

from ewoksfluo import __version__ as version


logger = logging.getLogger(__name__)


def split_h5uri(url: str) -> Tuple[str, str]:
    obj = DataUrl(url)
    return obj.file_path(), obj.data_path() or ""


def create_data(
    parent: Union[h5py.File, h5py.Group],
    name: str,
    signal: Optional[str] = None,
) -> h5py.Group:
    nxdata = parent.create_group(name)
    nxdata.attrs["NX_class"] = "NXdata"
    if signal:
        nxdata.attrs["signal"] = signal
    nexus.select_default_plot(nxdata)
    return nxdata


def set_data_signals(nxdata: h5py.Group, signals: Sequence[str]):
    nxdata.attrs["signal"] = signals[0]
    if len(signals) > 1:
        nxdata.attrs["auxiliary_signals"] = signals[1:]


def now() -> str:
    """NeXus-compliant format of the current time"""
    return datetime.now().astimezone().isoformat()


@contextlib.contextmanager
def save_in_ewoks_process(
    output_uri: str,
    start_time: str,
    process_config: Dict[str, Any],
    default_levels=("results", "process"),
    **kw
) -> Generator[h5py.Group, None, None]:
    with nexus.create_nexus_group(output_uri, default_levels=default_levels, **kw) as (
        process_group,
        _,
    ):
        entry_name = process_group.name.split("/")[1]
        entry_group = process_group.file[entry_name]
        if "start_time" not in entry_group:
            entry_group["start_time"] = start_time

        try:
            process_group["program"] = "ewoksfluo"
            process_group["version"] = version
            config_group = process_group.create_group("configuration")
            config_group.attrs["NX_class"] = "NXnote"
            config_group.create_dataset(
                "data", data=json.dumps(process_config, cls=NumpyEncoder)
            )
            config_group.create_dataset("date", data=now())
            config_group.create_dataset("type", data="json")

            yield process_group
        finally:
            if "end_time" in entry_group:
                entry_group["end_time"][()] = now()
            else:
                entry_group["end_time"] = now()


@contextlib.contextmanager
def save_in_ewoks_subprocess(
    output_uri: str,
    start_time: str,
    process_config: Dict[str, Any],
    collection_name: str = "results",
    **kw
):
    with save_in_ewoks_process(output_uri, start_time, process_config, **kw) as process:
        results = process.create_group(collection_name)
        results.attrs["NX_class"] = "NXcollection"
        yield results


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (numpy.generic, numpy.ndarray)):
            return obj.tolist()
        return super().default(obj)
