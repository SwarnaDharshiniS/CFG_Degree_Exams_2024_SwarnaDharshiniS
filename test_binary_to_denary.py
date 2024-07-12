import unittest
from alt_exam_python import bin2den, InvalidBinaryStringError

class TestBin2Den(unittest.TestCase):
    def test_valid_binary_strings(self):
        self.assertEqual(bin2den("110011"), 51)
        self.assertEqual(bin2den("111111"), 63)
        self.assertEqual(bin2den("1010"), 10)
        self.assertEqual(bin2den("1"), 1)
        self.assertEqual(bin2den("0"), 0)

    def test_invalid_binary_strings(self):
        with self.assertRaises(InvalidBinaryStringError):
            bin2den("110021")
        with self.assertRaises(InvalidBinaryStringError):
            bin2den("abc")
        with self.assertRaises(InvalidBinaryStringError):
            bin2den("")

    def test_edge_cases(self):
        self.assertEqual(bin2den("0000"), 0)
        self.assertEqual(bin2den("0001"), 1)
        self.assertEqual(bin2den("1000"), 8)

if __name__ == "__main__":
    unittest.main()
