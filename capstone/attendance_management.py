class AttendanceSystem:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, date, student_id, status):
        if date not in self.records:
            self.records[date] = {}
        self.records[date][student_id] = status

    def get_attendance(self, date, student_id):
        return self.records.get(date, {}).get(student_id)
