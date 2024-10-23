class Question:
    def __init__(self,q_text,q_answer) :
        self.text=q_text
        self.answer=q_answer
        self.score=0
    # def __repr__(self):
    #     return f"Question(text='{self.text}', answer='{self.answer}')"