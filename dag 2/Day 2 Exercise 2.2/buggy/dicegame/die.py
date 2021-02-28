# Just count the stupid dice
import random

##def roll(dice):                                               removed it altogether
##    for die in dice:
##        # XXX: I don't even know what this function does
##        continue

class Die:
    """
    This is always correct. Seriously, look away.
    """

    def __init__(self):
        self.roll()

    def roll(self):
        self.value = int(random.random() * 6 + 1)

    def show(self):
        if self.value == 1:
            return("---------\n|       |\n|   *   |\n|       |\n---------")
        elif self.value == 2:
            return("---------\n|*      |\n|       |\n|      *|\n---------")
        elif self.value == 3:
            return("---------\n|*      |\n|   *   |\n|      *|\n---------")
        elif self.value == 4:
            return("---------\n|*     *|\n|       |\n|*     *|\n---------")
        elif self.value == 5:
            return("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
        else:
            return("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

    @classmethod
    def create_dice(self, n):                           #replaced cls for self on two lines
        return [self() for _ in range(n)]
