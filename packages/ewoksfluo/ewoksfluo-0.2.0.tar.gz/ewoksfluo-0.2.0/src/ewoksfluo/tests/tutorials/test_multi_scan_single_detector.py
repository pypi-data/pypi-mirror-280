from typing import List, Dict
from ewoksorange.bindings import ows_to_ewoks
from ewokscore import execute_graph

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files


def test_multi_scan_single_detector_without_qt(tmpdir):
    from orangecontrib.ewoksfluo.categories.demo import tutorials

    filename = resource_files(tutorials).joinpath("mesh_multi_scan_single_detector.ows")
    assert_multi_scan_single_detector_without_qt(filename, tmpdir)


def test_multi_scan_single_detector_with_qt(ewoks_orange_canvas, tmpdir):
    from orangecontrib.ewoksfluo.categories.demo import tutorials

    filename = resource_files(tutorials).joinpath("mesh_multi_scan_single_detector.ows")
    assert_multi_scan_single_detector_with_qt(ewoks_orange_canvas, filename, tmpdir)


def assert_multi_scan_single_detector_without_qt(filename, tmpdir):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph, inputs=get_inputs(tmpdir), outputs=[{"all": True}], merge_outputs=False
    )
    expected = get_expected_outputs(tmpdir)
    label_to_id = {
        attrs["label"]: node_id for node_id, attrs in graph.graph.nodes.items()
    }
    expected = {label_to_id[k]: v for k, v in expected.items()}
    assert outputs == expected


def assert_multi_scan_single_detector_with_qt(ewoks_orange_canvas, filename, tmpdir):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=get_inputs(tmpdir))
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=10)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    assert outputs == get_expected_outputs(tmpdir)


def get_inputs(tmpdir) -> List[dict]:
    return [
        {
            "label": "Mesh: N scan, 1 det",
            "name": "output_filename",
            "value": str(tmpdir / "input.h5"),
        },
        {
            "label": "Fit: N scan, 1 det",
            "name": "output_uri_template",
            "value": str(tmpdir / "output.h5::/1.1"),
        },
    ]


def get_expected_outputs(tmpdir) -> Dict[str, dict]:
    return {
        "Mesh: N scan, 1 det": {
            "config": str(tmpdir / "input.h5::/1.1/theory/configuration/data"),
            "detector_name": "mca0",
            "expo_time": 0.1,
            "filenames": [str(tmpdir / "input.h5")],
            "monitor_name": "I0",
            "monitor_reference_values": [1000000] * 3,
            "scan_ranges": [[1, 3]],
        },
        "Pick scans": {
            "scan_uris": [str(tmpdir / f"input.h5::/{i}.1") for i in range(1, 4)]
        },
        "Fit: N scan, 1 det": {
            "fit_results_uri": str(tmpdir / "output.h5::/1.1/fit/results")
        },
    }
