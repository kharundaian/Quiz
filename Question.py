class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def getPrompt(self):
        return self.prompt

    def getAnswer(self):
        return self.answer