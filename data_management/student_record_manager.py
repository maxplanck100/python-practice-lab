class StudentRecordManager:
    def __init__(self):
        self.records = {}

    def add_record(self, student_id, name, age):
        self.records[student_id] = {"name": name, "age": age}

    def get_record(self, student_id):
        return self.records.get(student_id)
