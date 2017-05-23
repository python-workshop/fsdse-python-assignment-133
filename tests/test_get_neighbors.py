from unittest import TestCase
from bst import Node
from results import Results


class TestGet_neighbors(TestCase):
    def test_bfs(self):
        try:
            from build import BstBfs
        except ImportError:
            self.assertEqual("no class found")

        self.results = Results()

        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')
