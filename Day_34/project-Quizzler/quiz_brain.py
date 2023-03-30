import html
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0


    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def NextQuestion(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number+=1
        q_text = html.unescape(self.current_question.text) #unescaping
        return f"Q.{self.question_number}: {q_text} (True/False)?: "

    def check_ans(self,user_ans):
        if  user_ans == self.current_question.ans:
            self.score+=1
            return True
        else:
            return False
        