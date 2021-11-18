#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer


#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndext = 0

    def getQuestion(self):
        return self.questions[self.questionIndext]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru {self.questionIndext +1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if(question.checkAnswer(answer)):
            self.score += 1
        self.questionIndext += 1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndext:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print(f"Score: {self.score}")

    def displayProgress(self):
        totalQuestions = len(self.questions)
        questionNumber = self.questionIndext+1

        if questionNumber> totalQuestions:
            print("Sorular Bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestions}".center(100,"*"))

q1 = Question("En iyi programlama dili hangisidir ?", ["c#","Python","JS","java"],"Python")
q2 = Question("En popüler programlama dili hangisidir ?", ["c#","Python","JS","java"],"java")
q3 = Question("En eski programlama dili hangisidir ?", ["c#","Python","JS","java"],"JS")
print(q1.checkAnswer("Python"))
print(q2.checkAnswer("JS"))
print(q3.checkAnswer("JS"))
questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.loadQuestion()