"""module used to make ease refactoring"""

from darfix import dtypes
from typing import Union


def fromOWSendDatasetToDataset(
    dataset: Union[dtypes.OWDataset, dtypes.OWSendDataset, dtypes.Dataset]
) -> dtypes.Dataset:
    """
    util function to handle compatibility between widgets
    """
    if isinstance(dataset, dtypes.OWSendDataset):
        dataset, _ = dataset

    return dataset


def fromDatasetToOWSendDataset(
    dataset: Union[dtypes.OWDataset, dtypes.OWSendDataset, dtypes.Dataset], parent=None
) -> dtypes.OWSendDataset:
    """
    util function to handle compatibility between widgets
    """
    if isinstance(dataset, dtypes.Dataset):
        dataset = dtypes.OWDataset(
            dataset=dataset.dataset,
            indices=dataset.indices,
            bg_dataset=dataset.bg_dataset,
            bg_indices=dataset.bg_indices,
            parent=parent,
        )
    if isinstance(dataset, dtypes.OWDataset):
        dataset = dtypes.OWSendDataset(
            dataset=dataset,
            update=None,
        )
    return dataset
