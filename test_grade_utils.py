import unittest

from grade_utils import average, grade, highest, percentage, remove_failed


class TestAverage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(average([80, 90, 100]), 90)

    def test_float_result(self):
        self.assertAlmostEqual(average([1, 2]), 1.5)

    def test_single_value(self):
        self.assertEqual(average([50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(average([-10, -20, -30]), -20)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            average([])


class TestGrade(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(grade(95), "A")
        self.assertEqual(grade(85), "B")
        self.assertEqual(grade(75), "C")
        self.assertEqual(grade(50), "D")

    def test_boundaries(self):
        self.assertEqual(grade(100), "A")
        self.assertEqual(grade(90), "A")
        self.assertEqual(grade(89.9), "B")
        self.assertEqual(grade(80), "B")   # was "C" in the buggy version
        self.assertEqual(grade(79.9), "C")
        self.assertEqual(grade(70), "C")
        self.assertEqual(grade(69.9), "D")
        self.assertEqual(grade(0), "D")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            grade(-1)
        with self.assertRaises(ValueError):
            grade(101)


class TestHighest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(highest([45, 92, 67]), 92)

    def test_single_value(self):
        self.assertEqual(highest([7]), 7)

    def test_duplicates(self):
        self.assertEqual(highest([88, 88, 12]), 88)

    def test_all_negative(self):
        self.assertEqual(highest([-5, -2, -9]), -2)   # buggy version returned 0

    def test_all_zero(self):
        self.assertEqual(highest([0, 0]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            highest([])


class TestPercentage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(percentage(45, 50), 90)   # buggy version returned 0

    def test_fraction(self):
        self.assertAlmostEqual(percentage(1, 3), 33.333333, places=5)

    def test_full_and_zero(self):
        self.assertEqual(percentage(50, 50), 100)
        self.assertEqual(percentage(0, 50), 0)

    def test_zero_total(self):
        with self.assertRaises(ValueError):
            percentage(10, 0)

    def test_negative_total(self):
        with self.assertRaises(ValueError):
            percentage(10, -5)


class TestRemoveFailed(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(remove_failed([20, 50, 10, 80]), [50, 80])

    def test_consecutive_failures(self):
        # buggy version skipped elements and returned [20, 50]
        self.assertEqual(remove_failed([10, 20, 50]), [50])

    def test_boundary_pass_mark(self):
        self.assertEqual(remove_failed([32, 33, 34]), [33, 34])

    def test_custom_pass_mark(self):
        self.assertEqual(remove_failed([40, 50, 60], pass_mark=50), [50, 60])

    def test_all_fail(self):
        self.assertEqual(remove_failed([1, 2, 3]), [])

    def test_negative_numbers(self):
        self.assertEqual(remove_failed([-5, 40, -1]), [40])

    def test_empty_list(self):
        self.assertEqual(remove_failed([]), [])

    def test_input_not_modified(self):
        marks = [10, 50, 20]
        remove_failed(marks)
        self.assertEqual(marks, [10, 50, 20])


if __name__ == "__main__":
    unittest.main()
