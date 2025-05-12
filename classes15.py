# Online Course Enrollment System
class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.students = []

    def enroll(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has enrolled in {self.name}")

    def course_info(self):
        print(f"Course: {self.name}, Instructor: {self.instructor}, Students: {len(self.students)}")

c1 = Course("Python Programming", "Mr. Shah")
c1.enroll("Jenish")
c1.enroll("Amit")
c1.course_info()
