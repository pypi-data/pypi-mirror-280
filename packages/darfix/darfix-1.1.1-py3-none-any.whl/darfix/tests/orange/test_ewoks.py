import h5py
import numpy
import os
from silx.io.url import DataUrl
from silx.resources import ExternalResources

from ewoks import load_graph
from ewoksorange.bindings import ows_to_ewoks
from ewokscore import execute_graph

from darfix.core.grainplot import MomentType
from darfix.core.process import (
    DataSelection,
    DimensionDefinition,
    RoiSelection,
    generate_ewoks_task_inputs,
)
from darfix.tasks.grainplot import GrainPlot
from darfix.tasks.noiseremoval import NoiseRemoval

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files


def test_darfix_example2_edf(tmpdir):
    from orangecontrib.darfix import tutorials

    filename = resource_files(tutorials).joinpath("darfix_example2.ows")

    image0 = resource_files(tutorials).joinpath("edf_dataset", "strain_0000.edf")
    image1 = resource_files(tutorials).joinpath("edf_dataset", "strain_0001.edf")
    filenames = [str(image0), str(image1)]
    inputs = generate_ewoks_task_inputs(
        DataSelection,
        filenames=filenames,
        root_dir=str(tmpdir),
        in_memory=True,
    )
    graph = load_graph(str(filename), inputs=inputs)

    results = graph.execute(output_tasks=True)
    for node_id, task in results.items():
        assert task.succeeded, node_id


def test_darfix_example2_hdf5(tmpdir):
    from orangecontrib.darfix import tutorials

    filename = resource_files(tutorials).joinpath("darfix_example2.ows")

    hdf5_dataset_file = resource_files(tutorials).joinpath(
        "hdf5_dataset", "strain.hdf5"
    )
    assert os.path.exists(str(hdf5_dataset_file))
    filenames = (
        DataUrl(
            file_path=str(hdf5_dataset_file),
            data_path="/1.1/instrument/my_detector/data",
            scheme="silx",
        ).path(),
    )
    inputs = generate_ewoks_task_inputs(
        DataSelection,
        filenames=filenames,
        root_dir=str(tmpdir),
        in_memory=False,
        metadata_url=DataUrl(
            file_path=str(hdf5_dataset_file),
            data_path="/1.1/instrument/positioners",
            scheme="silx",
        ).path(),
    )
    graph = load_graph(str(filename), inputs=inputs)

    results = graph.execute(output_tasks=True)
    for node_id, task in results.items():
        assert task.succeeded, node_id


def get_inputs(input_filename: str):
    ds_inputs = generate_ewoks_task_inputs(
        DataSelection,
        metadata_url=DataUrl(
            file_path=input_filename,
            data_path="/2.1/instrument/positioners",
            scheme="silx",
        ),
        raw_filename=DataUrl(
            file_path=input_filename,
            data_path="/2.1/instrument/my_detector/data",
            scheme="silx",
        ),
    )
    dim_inputs = generate_ewoks_task_inputs(
        DimensionDefinition,
        _dims={
            0: {"name": "diffry", "kind": 2, "size": 8, "tolerance": 1e-09},
            1: {"name": "diffrx", "kind": 2, "size": 9, "tolerance": 1e-09},
        },
    )
    roi_inputs = generate_ewoks_task_inputs(
        RoiSelection, roi_origin=[198, 114], roi_size=[59, 133]
    )
    noise_inputs = generate_ewoks_task_inputs(
        NoiseRemoval,
        method="median",
        background_type="Data",
        bottom_threshold=0,
        chunks=[100, 100],
        kernel_size=3,
    )

    return [*ds_inputs, *dim_inputs, *roi_inputs, *noise_inputs]


def test_example_workflow2(tmpdir):
    """Execute workflow after converting it to an ewoks workflow"""
    silx_resources = ExternalResources(
        "darfix", url_base="http://www.silx.org/pub/darfix"
    )
    silx_resources._data_home = tmpdir
    ref_filename = silx_resources.getfile("maps.h5")

    from orangecontrib.darfix import tutorials

    filename = resource_files(tutorials).joinpath("darfix_example2.ows")

    graph = ows_to_ewoks(filename)
    input_filename = silx_resources.getfile("input.h5")
    output_filename = str(tmpdir / "maps.h5")
    inputs = [
        *get_inputs(input_filename),
        *generate_ewoks_task_inputs(GrainPlot, filename=output_filename),
    ]
    positioners = ("diffrx", "diffry")

    execute_graph(graph, inputs=inputs, outputs=[{"all": True}], merge_outputs=False)

    with h5py.File(ref_filename, "r") as ref_file:
        with h5py.File(output_filename, "r") as output_file:
            ref_entry = ref_file["entry"]
            output_entry = output_file["entry"]
            assert list(output_entry.keys()) == [
                "Mosaicity",
                "Orientation distribution",
                *positioners,
            ]

            for pos in positioners:
                for moment in MomentType.values():
                    numpy.testing.assert_allclose(
                        ref_entry[pos][moment][moment],
                        output_entry[pos][moment][moment],
                    )

            numpy.testing.assert_allclose(
                ref_entry["Mosaicity/Mosaicity"], output_entry["Mosaicity/Mosaicity"]
            )
            numpy.testing.assert_allclose(
                ref_entry["Orientation distribution/key/image"],
                output_entry["Orientation distribution/key/image"],
            )
