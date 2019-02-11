#!/usr/bin/python

import unittest

import sierpinski_triangle as st


class TestSierpinskiTriangle(unittest.TestCase):

    def test_step_count(self):
        obj = st.SierpinskiTriangle()
        self.assertEqual(obj.steps, 0)
        obj.Step()
        self.assertEqual(obj.steps, 1)
