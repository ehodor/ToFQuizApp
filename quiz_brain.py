import html

class QuizBrain:
    def __init__(self, list1):
        self.q_number = 0
        self.q_list = list1
        self.score = 0

    def still_q(self):
        return self.q_number < (len(self.q_list))

    def next_q(self):
        q_text = html.unescape(self.q_list[self.q_number].text)
        #user_answer = input(f'Q {self.q_number + 1}: {q_text} (True or False?): ').lower()
        self.q_number += 1
        return  f"Q {self.q_number}: {q_text}"
        #self.check(user_answer, self.q_list[self.q_number].answer)

    def next_q_answer(self):
        q_text = html.unescape(self.q_list[self.q_number-1].answer)
        #user_answer = input(f'Q {self.q_number + 1}: {q_text} (True or False?): ').lower()
        #self.q_number += 1
        return  q_text
        #self.check(user_answer, self.q_list[self.q_number].answer)
    def check(self, user_answer, cor_answer):
        if user_answer.lower() == cor_answer.lower():
            self.score += 1
            print('Right!')
            print(f'Your current score is: {self.score}/{self.q_number}')
            print('\n')
            return True
        print('Wrong!')
        print(f'The correct answer was: {cor_answer}')
        print(f'Your current score is: {self.score}/{self.q_number}')
        print('\n')
        return False
