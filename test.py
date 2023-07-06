import unittest
from shapely.geometry import Polygon
from base import (
    PlyShape,
    PickResult,
    Report,
    compactness,
    picks_failures,
    picks_primary_failure_reason,
    picks_first_valid
)


class Test(unittest.TestCase):

    def test_compactness(self):
        # Create a test polygon
        polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])

        # Test the compactness function
        result = compactness(polygon)

        # Assert the result is within the expected range
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 100.0)

    def test_picks_failures(self):
        # Create some sample PickResult objects
        pick1 = PickResult(valid=True)
        pick2 = PickResult(valid=False)
        pick3 = PickResult(valid=False)

        # Create a list of PickResults
        picks = [pick1, pick2, pick3]

        # Test the picks_failures function
        result = picks_failures(picks)

        # Assert that the list only contains the invalid picks
        self.assertEqual(result, [pick2, pick3])

    def test_picks_primary_failure_reason(self):
        # Create some sample PickResult objects
        pick1 = PickResult(valid=False, reason="Failure-Reason1")
        pick2 = PickResult(valid=False, reason="Failure-Reason2")
        pick3 = PickResult(valid=False, reason="Failure-Reason1")

        # Create a list of PickResults
        picks = [pick1, pick2, pick3]

        # Test the picks_primary_failure_reason function
        result = picks_primary_failure_reason(picks)

        # Assert that the most common failure reason is returned
        self.assertEqual(result, "Reason1")

    def test_picks_first_valid(self):
        # Create some sample PickResult objects
        pick1 = PickResult(valid=False)
        pick2 = PickResult(valid=True)
        pick3 = PickResult(valid=False)

        # Create a list of PickResults
        picks = [pick1, pick2, pick3]

        # Test the picks_first_valid function
        result = picks_first_valid(picks)

        # Assert that the first valid pick is returned
        self.assertEqual(result, pick2)


if __name__ == '__main__':
    unittest.main()
