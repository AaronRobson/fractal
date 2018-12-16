#!/usr/bin/python

import unittest

import sierpinski_triangle_gui as st_gui


class TestSierpinskiTriangleGUI(unittest.TestCase):

    def test_gui(self):
        gui = st_gui.GUI()
        gui.Reset()


if __name__ == "__main__":
    unittest.main()
