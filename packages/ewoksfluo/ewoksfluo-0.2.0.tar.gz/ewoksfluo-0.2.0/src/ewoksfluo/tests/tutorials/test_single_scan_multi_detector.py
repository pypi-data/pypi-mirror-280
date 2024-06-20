from typing import List, Dict
from ewoksorange.bindings import ows_to_ewoks
from ewokscore import execute_graph

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files


def test_single_scan_multi_detector_without_qt(tmpdir):
    from orangecontrib.ewoksfluo.categories.demo import tutorials

    filename = resource_files(tutorials).joinpath("mesh_single_scan_multi_detector.ows")
    assert_single_scan_multi_detector_without_qt(filename, tmpdir)


def test_single_scan_multi_detector_with_qt(ewoks_orange_canvas, tmpdir):
    from orangecontrib.ewoksfluo.categories.demo import tutorials

    filename = resource_files(tutorials).joinpath("mesh_single_scan_multi_detector.ows")
    assert_single_scan_multi_detector_with_qt(ewoks_orange_canvas, filename, tmpdir)


def assert_single_scan_multi_detector_without_qt(filename, tmpdir):
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


def assert_single_scan_multi_detector_with_qt(ewoks_orange_canvas, filename, tmpdir):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=get_inputs(tmpdir))
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=10)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    assert outputs == get_expected_outputs(tmpdir)


def get_inputs(tmpdir) -> List[dict]:
    return [
        {
            "label": "Mesh: 1 scan, N det",
            "name": "output_filename",
            "value": str(tmpdir / "input.h5"),
        },
        {
            "label": "Fit: 1 scan, N det",
            "name": "output_uri_template",
            "value": str(tmpdir / "output.h5::/1.1/fit/{}"),
        },
        {
            "label": "Sum Fit Results",
            "name": "output_uri",
            "value": str(tmpdir / "output.h5::/1.1"),
        },
        {
            "label": "Regrid",
            "name": "output_uri",
            "value": str(tmpdir / "output.h5::/1.1"),
        },
    ]


def get_expected_outputs(tmpdir) -> Dict[str, dict]:
    return {
        "Mesh: 1 scan, N det": {
            "config": str(tmpdir / "input.h5::/1.1/theory/configuration/data"),
            "configs": [str(tmpdir / "input.h5::/1.1/theory/configuration/data")] * 2,
            "detector_names": ["mca0", "mca1"],
            "expo_time": 0.1,
            "filename": str(tmpdir / "input.h5"),
            "monitor_name": "I0",
            "monitor_reference_value": 1000000,
            "scan_number": 1,
        },
        "Pick scan": {"scan_uri": str(tmpdir / "input.h5::/1.1")},
        "Fit: 1 scan, N det": {
            "fit_results_uris": [
                str(tmpdir / "output.h5::/1.1/fit/mca0/results"),
                str(tmpdir / "output.h5::/1.1/fit/mca1/results"),
            ]
        },
        "Sum Fit Results": {
            "summed_results_uri": str(tmpdir / "output.h5::/1.1/sumfit/results")
        },
        "Regrid": {"regridded_uri": str(tmpdir / "output.h5::/1.1/regrid")},
    }
