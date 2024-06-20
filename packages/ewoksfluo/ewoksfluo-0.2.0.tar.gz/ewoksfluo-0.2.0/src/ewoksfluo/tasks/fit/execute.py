from queue import Queue
from typing import Dict, List, Optional, Sequence, Set, Tuple, Union
from concurrent.futures import ProcessPoolExecutor
from contextlib import ExitStack
import multiprocessing

from PyMca5.PyMcaIO.ConfigDict import ConfigDict

from ... import h5_subprocess

from ...xrffit import perform_batch_fit
from ...xrffit import outputbuffer_context
from ...xrffit import queue_outputbuffer_context

from ...xrffit.handlers import NexusOutputHandler
from ...xrffit.handlers import consume_handler_queue
from ...xrffit.handlers import stop_queue


def fit_single(
    scan_uri: str,
    xrf_spectra_uri_template: str,
    output_uri_template: str,
    detector_name: str,
    config: Union[str, ConfigDict],
    energy: Optional[float] = None,
    quantification: Optional[dict] = None,
    energy_multiplier: Optional[float] = None,
    fast_fitting: bool = False,
    diagnostics: bool = False,
    figuresofmerit: Optional[bool] = None,
) -> str:
    """Fitting of one scan with one detector.

    Returns the URL of the fit result.
    """
    if figuresofmerit is None:
        figuresofmerit = diagnostics
    output_uri = output_uri_template.format(detector_name)
    with outputbuffer_context(
        output_uri,
        diagnostics=diagnostics,
        figuresofmerit=figuresofmerit,
    ) as output_buffer:
        if output_buffer.already_existed:
            print(f"{output_buffer.fit_results_uri} already exists")
        else:
            xrf_spectra_uri = (
                f"{scan_uri}/{xrf_spectra_uri_template.format(detector_name)}"
            )
            perform_batch_fit(
                xrf_spectra_uris=[xrf_spectra_uri],
                cfg=config,
                output_buffer=output_buffer,
                energy=energy,
                energy_multiplier=energy_multiplier,
                quantification=quantification,
                fast=fast_fitting,
            )
        return output_buffer.fit_results_uri


def fit_multi(
    scan_uris: Sequence[str],
    xrf_spectra_uri_template: str,
    output_uri_template: str,
    detector_names: Sequence[str],
    configs: Sequence[Union[str, ConfigDict]],
    energies: Optional[Sequence[Optional[float]]] = None,
    quantification: Optional[dict] = None,
    energy_multiplier: Optional[float] = None,
    fast_fitting: bool = False,
    diagnostics: bool = False,
    figuresofmerit: Optional[bool] = None,
) -> List[str]:
    """Parallelized fitting of multiple scans with multiple detectors.

    Returns the URL's of the fit result (one URL per detector).
    """
    nscans = len(scan_uris)
    if energies:
        if len(energies) != nscans:
            raise ValueError(f"Requires {nscans} energies, one for each scan")
    else:
        energies = [None] * nscans
    ndetectors = len(detector_names)
    if len(configs) != ndetectors:
        raise ValueError(
            f"Requires {ndetectors} pymca configurations, one for each detector"
        )

    if figuresofmerit is None:
        figuresofmerit = diagnostics
    if diagnostics:
        default_group = "fit"
    else:
        default_group = "parameters"

    fit_results_uris: List[str] = []

    with ExitStack() as stack:
        mp_context = multiprocessing.get_context(method="spawn")
        ctx = mp_context.Manager()
        manager = stack.enter_context(ctx)
        queue = manager.Queue()

        ctx = ProcessPoolExecutor(
            mp_context=mp_context, initializer=h5_subprocess.initializer
        )
        executor = stack.enter_context(ctx)

        arguments: List[Tuple[tuple, dict, dict]] = list()
        output_handlers: Dict[int, NexusOutputHandler] = dict()
        queue_sendids: Set[int] = set()

        output_uris = [
            output_uri_template.format(detector_name)
            for detector_name in detector_names
        ]
        if len(set(output_uris)) != len(output_uris):
            raise ValueError(
                "Add a place-holder '{}' for the detector name in the output URI template"
            )
        xrf_spectra_uris = [
            [
                f"{scan_uri}/{xrf_spectra_uri_template.format(detector_name)}"
                for scan_uri in scan_uris
            ]
            for detector_name in detector_names
        ]
        if len(set(xrf_spectra_uris[0])) != len(xrf_spectra_uris[0]):
            raise ValueError(
                "Add a place-holder '{}' for the detector name in the XRF spectra URI template"
            )

        for destinationid, (output_uri, detector_spectra_uris, config) in enumerate(
            zip(output_uris, xrf_spectra_uris, configs)
        ):
            ctx = NexusOutputHandler(output_uri, default_group=default_group)
            output_handler = stack.enter_context(ctx)
            fit_results_uris.append(output_handler.fit_results_uri)
            if output_handler.already_existed:
                print(f"{output_handler.fit_results_uri} already exists")
                continue
            output_handlers[destinationid] = output_handler

            for i_scan, (xrf_spectra_uri, energy) in enumerate(
                zip(detector_spectra_uris, energies)
            ):
                queue_sendid = destinationid * nscans + i_scan
                queue_sendids.add(queue_sendid)

                buffer_args = (
                    queue,
                    queue_sendid,
                    destinationid,
                    nscans,
                    i_scan,
                )
                buffer_kwargs = {
                    "diagnostics": diagnostics,
                    "figuresofmerit": figuresofmerit,
                }
                fit_kwargs = {
                    "xrf_spectra_uris": [xrf_spectra_uri],
                    "cfg": config,
                    "energy": energy,
                    "energy_multiplier": energy_multiplier,
                    "quantification": quantification,
                    "fast": fast_fitting,
                }
                arguments.append(
                    (
                        _fit_main.__module__,
                        _fit_main.__name__,
                        buffer_args,
                        buffer_kwargs,
                        fit_kwargs,
                    )
                )

        if not arguments:
            return fit_results_uris

        # Sub-processes will fit send the results to the queue
        futures = {
            i: executor.submit(h5_subprocess.main, *args)
            for i, args in enumerate(arguments)
        }

        def raise_on_error():
            nonlocal futures
            for i, future in list(futures.items()):
                if future.done():
                    future.result()  # re-raise exception (if any)
                    futures.pop(i)

        # Main process will receive results from the queue and save them in HDF5
        consume_handler_queue(output_handlers, queue, queue_sendids, raise_on_error)

        # Re-raise exceptions (if any)
        for future in futures.values():
            future.result()

    return fit_results_uris


def _fit_main(
    buffer_args: Tuple[Queue, int, int, Optional[int], int],
    buffer_kwargs: dict,
    fit_kwargs: dict,
) -> None:
    queue, sendid, destinationid, nscans, scan_index = buffer_args
    if nscans == 1:
        nscans = None
        scan_index = None
    try:
        with queue_outputbuffer_context(
            queue,
            sendid,
            destinationid,
            nscans=nscans,
            scan_index=scan_index,
            **buffer_kwargs,
        ) as output_buffer:
            perform_batch_fit(output_buffer=output_buffer, **fit_kwargs)
    finally:
        stop_queue(queue, sendid)
