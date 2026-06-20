class QuizPlatform:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, answer):
        self.questions.append({"q": question, "a": answer})

    def answer_question(self, index, answer):
        if 0 <= index < len(self.questions) and self.questions[index]["a"] == answer:
            self.score += 1
