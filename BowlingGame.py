class BowlingGame(object):
    def __init__(self):
        self.score = 0
        self.shots = []
        self.pins_in_frame = 10
        self.is_first_shot = True
        self.frame = 1
        self.game_over = False
        self.last_frame = 11

    def shot(self, pins: int):
        if not (0 <= pins <= self.pins_in_frame):
            raise ValueError("Wrong pins in a shot!")
        self.pins_in_frame -= pins
        if self.frame == self.last_frame:
            self.game_over = True
        elif self.frame == 11 and self.pins_in_frame == 0:
            self.last_frame = 12
        elif self.frame == 10 and self.pins_in_frame == 0:
            self.last_frame = 12
        if self.pins_in_frame <= 0 or not self.is_first_shot:
            self.pins_in_frame = 10
            self.frame += 1
            self.is_first_shot = True
        else:
            self.is_first_shot = False
        self.shots.append(pins)

    def calculate_score(self):
        ball = 0
        for _ in range(10):
            if self.shots[ball] == 10:
                self.score += 10 + self.shots[ball + 1] + self.shots[ball + 2]
                ball += 1
            elif self.shots[ball] + self.shots[ball + 1] == 10:
                self.score += 10 + self.shots[ball + 2]
                ball += 2
            else:
                self.score += self.shots[ball] + self.shots[ball + 1]
                ball += 2
        return self.score


if __name__ == "__main__":
    game = BowlingGame()
    while not game.game_over:
        pins = int(input("How many pins did you shot?"))
        game.shot(pins)
    print(game.shots)
    print(f"Scored: {game.calculate_score()}")
