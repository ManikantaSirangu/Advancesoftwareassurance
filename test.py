import unittest
from main import AttendanceSystem


class TestAttendanceSystem(unittest.TestCase):
    def setUp(self):
        self.attendance_system = AttendanceSystem()

        # Add classes
        self.attendance_system.add_class("CSCI101", "Introduction to Computer Science")
        self.attendance_system.add_class("MATH101", "Calculus")

        # Add students to classes
        self.attendance_system.add_student_to_class("CSCI101", "001", "Alice")
        self.attendance_system.add_student_to_class("CSCI101", "002", "Bob")
        self.attendance_system.add_student_to_class("MATH101", "001", "Alice")
        self.attendance_system.add_student_to_class("MATH101", "002", "Bob")

    def test_mark_attendance(self):
        # Mark attendance
        self.attendance_system.mark_attendance("CSCI101", "001", "2024-05-03", "Present")
        self.attendance_system.mark_attendance("CSCI101", "002", "2024-05-03", "Absent")
        self.attendance_system.mark_attendance("MATH101", "001", "2024-05-03", "Late")
        self.attendance_system.mark_attendance("MATH101", "002", "2024-05-03", "Present")

        # Check if attendance is marked correctly
        self.assertEqual(self.attendance_system.generate_report("CSCI101", "2024-05-03"),
                         {"001": "Present", "002": "Absent"})
        self.assertEqual(self.attendance_system.generate_report("MATH101", "2024-05-03"),
                         {"001": "Late", "002": "Present"})

    def test_get_student_attendance(self):
        # Mark attendance
        self.attendance_system.mark_attendance("CSCI101", "001", "2024-05-03", "Present")
        self.attendance_system.mark_attendance("MATH101", "002", "2024-05-03", "Present")

        # Check student attendance
        self.assertEqual(self.attendance_system.get_student_attendance("CSCI101", "001"),
                         {"2024-05-03": "Present"})
        self.assertEqual(self.attendance_system.get_student_attendance("MATH101", "002"),
                         {"2024-05-03": "Present"})

    def test_generate_report(self):
        # Mark attendance
        self.attendance_system.mark_attendance("CSCI101", "001", "2024-05-03", "Present")
        self.attendance_system.mark_attendance("CSCI101", "002", "2024-05-03", "Absent")
        self.attendance_system.mark_attendance("MATH101", "001", "2024-05-03", "Late")
        self.attendance_system.mark_attendance("MATH101", "002", "2024-05-03", "Present")

        # Generate report
        self.assertEqual(self.attendance_system.generate_report("CSCI101", "2024-05-03"),
                         {"001": "Present", "002": "Absent"})
        self.assertEqual(self.attendance_system.generate_report("MATH101", "2024-05-03"),
                         {"001": "Late", "002": "Present"})


if __name__ == "__main__":
    unittest.main()

