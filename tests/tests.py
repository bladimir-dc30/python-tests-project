import unittest
from src.calculator import *


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        assert add(20, 30) == 50

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_division(self):
        assert division(20, 4) == 5
        
    def test_multiplication(self):
        assert multiplication(10, 5) == 50