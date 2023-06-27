class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        input(f"Q.{self.question_num + 1}: {self.question_list[self.question_num].text} (True/False)?: ")
        self.question_num += 1
