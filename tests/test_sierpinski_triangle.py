#!/usr/bin/python

import unittest

import sierpinski_triangle as st


class TestSierpinskiTriangle(unittest.TestCase):

    def setUp(self):
        self.obj = st.SierpinskiTriangle()

    def test_step_count(self):
        self.assertEqual(self.obj.steps, 0)
        self.obj.Step()
        self.assertEqual(self.obj.steps, 1)

    def test_str(self):
        self.assertEqual(str(self.obj), '1\n((0.0, 0.0), (1.0, 0.0), (0.5, 0.8660254037844386))')
