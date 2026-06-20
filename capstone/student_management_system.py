class StudentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, details):
        self.students[student_id] = details

    def get_student(self, student_id):
        return self.students.get(student_id)
