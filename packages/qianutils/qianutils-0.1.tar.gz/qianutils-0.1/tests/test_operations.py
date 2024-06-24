import unittest
from qianutils.operations import reverse_string


class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")


if __name__ == '__main__':
    unittest.main()
