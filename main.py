class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def get_attendance(self):
        return self.attendance


class Class:
    def __init__(self, class_id, subject):
        self.class_id = class_id
        self.subject = subject
        self.students = {}

    def add_student(self, student_id, name):
        self.students[student_id] = Student(student_id, name)

    def mark_attendance(self, student_id, date, status):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, status)
        else:
            print(f"Student with ID {student_id} not found in the class.")

    def get_student_attendance(self, student_id):
        if student_id in self.students:
            return self.students[student_id].get_attendance()
        else:
            print(f"Student with ID {student_id} not found in the class.")
            return None


class AttendanceSystem:
    def __init__(self):
        self.classes = {}

    def add_class(self, class_id, subject):
        self.classes[class_id] = Class(class_id, subject)

    def add_student_to_class(self, class_id, student_id, name):
        if class_id in self.classes:
            self.classes[class_id].add_student(student_id, name)
        else:
            print(f"Class with ID {class_id} not found.")

    def mark_attendance(self, class_id, student_id, date, status):
        if class_id in self.classes:
            self.classes[class_id].mark_attendance(student_id, date, status)
        else:
            print(f"Class with ID {class_id} not found.")

    def get_student_attendance(self, class_id, student_id):
        if class_id in self.classes:
            return self.classes[class_id].get_student_attendance(student_id)
        else:
            print(f"Class with ID {class_id} not found.")
            return None

    def generate_report(self, class_id, date):
        if class_id in self.classes:
            class_attendance = self.classes[class_id]
            report = {}
            for student_id, student in class_attendance.students.items():
                if date in student.attendance:
                    report[student_id] = student.attendance[date]
            return report
        else:
            print(f"Class with ID {class_id} not found.")
            return None


def main():
    attendance_system = AttendanceSystem()

    # Add classes
    attendance_system.add_class("CSCI101", "Introduction to Computer Science")
    attendance_system.add_class("MATH101", "Calculus")

    # Add students to classes
    attendance_system.add_student_to_class("CSCI101", "001", "Alice")
    attendance_system.add_student_to_class("CSCI101", "002", "Bob")
    attendance_system.add_student_to_class("MATH101", "001", "Alice")
    attendance_system.add_student_to_class("MATH101", "002", "Bob")

    # Mark attendance
    attendance_system.mark_attendance("CSCI101", "001", "2024-05-03", "Present")
    attendance_system.mark_attendance("CSCI101", "002", "2024-05-03", "Absent")
    attendance_system.mark_attendance("MATH101", "001", "2024-05-03", "Late")
    attendance_system.mark_attendance("MATH101", "002", "2024-05-03", "Present")

    # Get student attendance
    print("Student 001 Attendance for CSCI101 on 2024-05-03:")
    print(attendance_system.get_student_attendance("CSCI101", "001"))

    # Generate report
    print("\nAttendance Report for CSCI101 on 2024-05-03:")
    print(attendance_system.generate_report("CSCI101", "2024-05-03"))


if __name__ == "__main__":
    main()
