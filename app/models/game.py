

class GameResult:
    def __init__(self, player_1: str, player_1_score: int, player_2: str, player_2_score: int):
        self.player_1 = player_1
        self.player_1_score = player_1_score
        self.player_2 = player_2
        self.player_2_score = player_2_score
    
    @property
    def score(self):
        if self.player_1_score == self.player_2_score:
            return {self.player_1 : 1, self.player_2 : 1}
        if self.player_1_score > self.player_2_score:
            return {self.player_1 : 3, self.player_2 : 0}
        return {self.player_1 : 0, self.player_2 : 3}
    
    def __str__(self):
        return f'<GameResult P1:{self.player_1} - {self.player_1_score}, P2:{self.player_2} - {self.player_2_score}/>'
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, o: object) -> bool:
        return isinstance(o, GameResult)  and \
            (self.player_1 == o.player_1) and \
            (self.player_1_score == o.player_1_score) & \
            (self.player_2 == o.player_2) & \
            (self.player_2_score == o.player_2_score)