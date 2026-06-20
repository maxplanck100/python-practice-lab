class NotesOrganizer:
    def __init__(self):
        self.notes = {}

    def add_note(self, title, content):
        self.notes[title] = content

    def get_note(self, title):
        return self.notes.get(title)
