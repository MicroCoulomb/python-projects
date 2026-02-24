import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False): ")
        # self.check_answer(user_answer, current_question.answer)
        # return {"Question": f"Q.{self.question_number}: {html.unescape(self.current_question.text)}",
        #         "Answer": self.current_question.answer}
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer):
        correct_answer = self.current_question.answer
        if u_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False