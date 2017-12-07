import unittest
# from mock import patch

from jenkinsDemo import Calcu

class TestMathFunc(unittest.TestCase):
    """Test Calcu.py"""
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, Calcu.add(1, 2))
        self.assertNotEqual(3, Calcu.add(2, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, Calcu.multi(2, 3))


if __name__ == '__main__':
    unittest.main()