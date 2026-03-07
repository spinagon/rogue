from domain.level import Level

class Session:
    MAX_LEVEL = 21

    def __init__(self):
        self.difficult = 1.0
        self.current_level = Level(self.difficult)
        self.level_number = 0
        self.score = 0

    def increase_score(self, points):
        pass
