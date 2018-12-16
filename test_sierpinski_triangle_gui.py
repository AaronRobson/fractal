#!/usr/bin/python

import unittest

import sierpinski_triangle_gui as st_gui


class TestSierpinskiTriangleGUI(unittest.TestCase):

    def test_flatten(self):
        expected = st_gui.Flatten([1, [2, 3, [4, 5, 6]]])
        self.assertEquals(expected, (1, 2, 3, 4, 5, 6))


if __name__ == "__main__":
    unittest.main()
