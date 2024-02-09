class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def check_answer(self, correct_answer, given_answer):
        return given_answer == correct_answer

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        if self.check_answer(current_question.answer.lower(), answer.lower()):
            self.score += 1
            print(f"You got it right! The answer was {current_question.answer}.")
        else:
            print(f"Sorry, you got it wrong The answer was {current_question.answer}.")
        print(f"Your score is {self.score}/{self.question_number}\n")

    def is_still_running(self):
        return self.question_number < len(self.questions)
