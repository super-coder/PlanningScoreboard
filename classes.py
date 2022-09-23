class Player:
    def __init__(self, name):
        self.name = name
        self.claim = 0
        self.score = 0

    def set_claim(self, claim):
        self.claim = claim

    def winner(self):
        self.score = self.score + self.claim * 10 + 10
