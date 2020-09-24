import random
from typing import Dict


class montyhall:
    def __init__(self, seed: int = None):
        if seed != None:
            random.seed(seed)
        self.doors = ['goat'] * 3
        self.carPos = None
        self.contestantPick = None

    def generateGame(self):
        self.doors = ['goat'] * 3
        self.carPos = random.randint(0, 2)
        self.doors[self.carPos] = 'car'
        self.contestantPick = random.randint(0, 2)

    def playGame(self) -> Dict[str, int]:
        self.results = {'switch': None, 'stay': None, 'randomize': None}

        # Generate the random decision by contestant: 0 -> stay, 1 -> switch
        randDecision = random.randint(0, 1)

        # Game master reveals a goat from one of the doors that the contestant did not pick
        if self.doors[self.contestantPick] == 'goat':
            # Wins a car by switching if the original pick was a goat
            self.results['switch'] = 1
            self.results['stay'] = 0
            self.results['randomize'] = (1 if randDecision == 1 else 0)
        else:
            # Wins nothing by switching if the original pick was already a car
            self.results['switch'] = 0
            self.results['stay'] = 1
            self.results['randomize'] = (1 if randDecision == 0 else 0)
        return self.results
