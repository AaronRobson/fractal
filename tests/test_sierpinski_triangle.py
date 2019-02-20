#!/usr/bin/python

import unittest

import sierpinski_triangle as st


class TestMeanAverage(unittest.TestCase):

    def test_two_values(self):
        self.assertAlmostEqual(st.MeanAverage(10, 20), 15)


class TestHalfPoint(unittest.TestCase):

    def test_two_values(self):
        actual = st.HalfPoint((0, 0), (1, 1))
        expected = (0.5, 0.5)
        self.assertEqual(len(actual), 2)
        self.assertAlmostEqual(actual[0], 0.5)
        self.assertAlmostEqual(actual[1], 0.5)


class TestSierpinskiTriangle(unittest.TestCase):

    def setUp(self):
        self.obj = st.SierpinskiTriangle()

    def test_step_count(self):
        self.assertEqual(self.obj.steps, 0)
        self.obj.Step()
        self.assertEqual(self.obj.steps, 1)

    def test_str(self):
        self.assertEqual(str(self.obj), '1\n((0.0, 0.0), (1.0, 0.0), (0.5, 0.8660254037844386))')
