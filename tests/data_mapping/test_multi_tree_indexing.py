import pytest
from pytest_lazyfixture import lazy_fixture
import uproot
# from fast_carpenter.tree_adapter import MultiTreeIndex
from fasthep_carpenter.data_mapping import MultiTreeIndex


@pytest.mark.parametrize(
    "path, prefix, expected",
    [
        (
            "tree1.s",
            "tree1",
            "tree1/s",
        ),
        (
            "tree1.folder.something",
            "tree1/folder/something",
            "tree1/folder/something",
        ),
        (
            "folder.something",
            "tree1",
            "tree1/folder/something",
        ),
    ]
)
def test_resolve_index(path, prefix, expected):
    indexer = MultiTreeIndex([prefix])
    index = indexer.resolve_index(path)
    assert index == expected
