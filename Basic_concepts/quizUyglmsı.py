# Question
class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
    
# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsİndex = 0

    def getQuestion(self):
        return self.questions[self.questionsİndex]
    
    def displayQuesiton(self):
        question = self.getQuestion()
        print(f"soru {self.questionsİndex + 1}: {question.text}")
        for q in question.choices:
            print(f"- " + q)
        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionsİndex += 1

        self.displayQuesiton()
    def loadQuestion(self):
        if len(self.question) == self.questionsİndex:
            self.showScore()
        else:
            self.displayQuesiton()

    def showScore(self):
        print("score: "+ self.score)







    # def guess(self, answer):
    #     question = self.getQuestion()
    #     if question.checkAnswer(answer):
    #         self.score += 1
    #     self.questionsİndex += 1

    

q1 = Question("en iyi programlama dili hangisidir? ", ['Python', 'java', 'Javascript', 'c#'], 'Python')
q2= Question("en popüler programlama dili hangisidir? ", ['java', 'Python', 'Javascript', 'c#'], 'Java')
q3 = Question("en çok kazandıran programlama dili hangisidir? ", ['c#', 'Python', 'java', 'Javascript'], 'c#')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.displayQuesiton()
