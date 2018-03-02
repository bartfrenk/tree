# pylint: disable=no-self-use, redefined-outer-name
import pytest
from tree import Tree


@pytest.fixture
def items():
    return [([1, 2, 3], 'x'), ([1, 2, 4], 'y'), ([5, 6], 'z')]


@pytest.fixture
def values(items):
    return [v for (_, v) in items]


@pytest.fixture
def paths(items):
    return [p for (p, _) in items]


class TestTreeGetAndSetItem(object):
    def test_get_returns_set_update_at_multiple_segments(self):
        t = Tree()
        t[range(10)] = 'x'
        assert t[range(10)] == 'x'

    def test_get_returns_set_update_at_single_segment(self):
        t = Tree()
        t[0] = 'x'
        assert t[0] == 'x'


class TestTreeIterators(object):
    def test_paths_of_empty_tree_is_the_empty_iterator(self):
        assert [] == list(Tree().paths())

    def test_values_of_empty_tree_is_the_empty_iterator(self):
        assert [] == list(Tree().values())

    def test_items_of_empty_tree_is_the_empty_iterator(self):
        assert [] == list(Tree().items())

    def test_items_iterates_over_all_path_value_pairs(self, items):
        assert sorted(items) == sorted(list(Tree.from_items(items).items()))

    def test_values_iterates_over_all_leaf_values(self, items, values):
        assert sorted(values) == sorted(list(Tree.from_items(items).values()))

    def test_paths_iterates_over_all_maximal_paths(self, items, paths):
        assert sorted(paths) == sorted(list(Tree.from_items(items).paths()))
