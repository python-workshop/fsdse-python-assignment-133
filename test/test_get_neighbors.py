from unittest import TestCase


class TestGet_neighbors(TestCase):
    def test_get_neighbors(self):
        try:
            from build import get_neighbors
        except ImportError:
            self.assertEqual("Import Error")

        res = get_neighbors(['c'])
        self.assertEqual('c',res)
