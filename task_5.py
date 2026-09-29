class Result:
    def __init__(self, victories, draws,losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Result):
    def __init__(self, victories, draws, losses):
        super().__init__ (victories, draws,losses)
    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}' 
    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'
    def total_points(self):
        return f'Общее количество очков: {3 * self.victories + self.draws}'   


class Hockey(Result):
    def __init__(self, victories, draws, losses):
        super().__init__ (victories, draws,losses)
    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}' 
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}' 
    def number_of_losses(self):
        return f'Хоккейных поражений: {self.losses}' 
    def total_points(self):
        return f'Общее количество очков:: {2 * self.victories + self.draws}'    


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

teams = [football_team, hockey_team]

for team in teams:
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
    print()