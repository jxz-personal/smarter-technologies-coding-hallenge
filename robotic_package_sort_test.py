import unittest
from robotic_package_sort import sort

class TestPackageSorting(unittest.TestCase):

    # --- STANDARD Stack Tests ---
    def test_standard_package(self):
        # Small dimensions and light weight
        self.assertEqual(sort(10, 10, 10, 10), "STANDARD")

    def test_standard_near_boundaries(self):
        # Just below the bulky and heavy limits
        self.assertEqual(sort(99, 99, 100, 19.9), "STANDARD")

    # --- SPECIAL Stack Tests (Bulky Only) ---
    def test_bulky_by_volume(self):
        # Volume exactly 1,000,000 but not heavy
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_by_dimension(self):
        # One dimension is 150 but volume is low and not heavy
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    # --- SPECIAL Stack Tests (Heavy Only) ---
    def test_heavy_only(self):
        # Mass is 20kg but dimensions are small
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    # --- REJECTED Stack Tests ---
    def test_rejected_package(self):
        # Both bulky (by dimension) and heavy
        self.assertEqual(sort(150, 20, 20, 25), "REJECTED")
        
    def test_rejected_by_volume_and_mass(self):
        # Both bulky (by volume) and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    # --- Edge Cases ---
    def test_minimum_values(self):
        # Smallest possible inputs
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")

if __name__ == "__main__":
    unittest.main()