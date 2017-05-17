from unittest import TestCase


class TestGet_neighbors(TestCase):
    # check if the value is false if none
    # check if the input is any should print the node
    def test_if_the_value_is_false_if_none(self):
        try:
            from build import get_neighbors
        except ImportError:
            self.assertEqual("Import Error")

        res = get_neighbors(None)
        self.assertEqual(False, res)

    def test_if_some_input_the_c_which_is_without_node_give_blank(self):
        try:
            from build import get_neighbors
        except ImportError:
            self.assertEqual("Import Error")

        res = get_neighbors(['c'])
        self.assertEqual([],res)

