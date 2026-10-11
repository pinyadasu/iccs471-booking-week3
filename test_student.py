"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking


class StudentMoveTests(unittest.TestCase):
    # A move may overlap its own old interval when no other booking blocks it.
    def test_overlapping_self_move_succeeds(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]
        result = move_booking(bookings, 17, "Room 201", 630, 690)
        self.assertIs(result, target)
        self.assertEqual(bookings, [Booking(17, "Room 201", 630, 690)])

    # Requesting the current room and interval succeeds without changing data.
    def test_unchanged_move_ignores_target_conflict(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]
        result = move_booking(bookings, 17, "Room 201", 600, 660)
        self.assertIs(result, target)
        self.assertEqual(bookings, [Booking(17, "Room 201", 600, 660)])

if __name__ == "__main__":
    unittest.main()
