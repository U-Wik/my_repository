from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total = total + die.value                           # not increment but added value
        return total

    @classmethod
    def run(self):                                              # not a bug as such but I change cls to self
                                                                # don't like "probably" i remove it
        runner = self()                                         # moved it here, from inside the loop, should be done once
        guessCount = 0                                          # variable namne changed from c to guessCount
        while True: 
            self.dice = Die.create_dice(5)                      # moved it here from __init__ to run it every turn

            print("\nRound {}\n".format(runner.round))           # added line

            for die in runner.dice:
                print(die.show())

            guess = ''                                          # rewrote some lines to catch errors
            while type(guess) != int:
                guess = input("Sigh. What is your guess?: ")
                try:
                    guess = int(guess)
                except ValueError:
                    print('Not a numer. Try again!')
 

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                guessCount += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                guessCount += 1                                             # (c or ) guessCount should be incremented
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1
            
            if guessCount == 6:
                print()                                                         # added line
                if runner.wins > runner.loses: print("You won... Congrats...")  # conditional ending
                else: print("You did not win....")                                # conditional ending
                
                print()                                                         # added line    
                prompt = input("Would you like to play again?[y/n]: ")          # now asking after all rounds

                if prompt == 'y' or prompt == 'Y':                       # replaced "" with "Y"
                    print()
                    runner.reset()                                          # resetting
                    guessCount = 0                                          # resetting
                    continue
                else:
                    break                             # strange ending changed to break
