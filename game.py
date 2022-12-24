"""
Purpose: Initialize a game of mastermind with an AI mastermind
Assignment: CS 108 Final Project
Author: Caleb Hurshman (cah222)
"""

import random

class MasterMind:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'pink']
        self.guesses_remaining = 10
        self.create_code()
        self.game_over = False
        self.player_wins = False
    
    def create_code(self):
        """ randomly create a sequence/code of 4 colors from the colors list """
        self.code = []
        for i in range(4):
            self.code.append(random.choice(self.colors))
        return self.code
            
    """def enter_guess(self):
        take input for a guess, TESTING PHASE ONLY
        self.guess = []
        for i in range(4):
            self.guess.append(input('Guess color (red, blue, green, yellow, orange, pink): ')) """
            
    def check_guess(self, guess, code):
        """ check if guess matches the code
        invariant: guess must be 4 entries long """
        if len(guess) == 4:
            if guess == code:
                self.player_wins = True
            else:
                self.player_wins = False
            return self.player_wins
        else:
            raise IndexError ("Make sure a guess contains 4 colored pins before submitting it")
            
    def give_feedback(self, guess):
        """ Compare code and guess lists """
        black_feedback = 0
        white_feedback = 0
        code_copy = self.code.copy()
        z = 0
        # find number of identically matching indexes in guess/code
        for i in range(0, 4):
            if guess[z] == code_copy[z]:
                black_feedback += 1
                code_copy.remove(code_copy[z])
                guess.remove(guess[z])
                z -= 1
            z += 1
        z = 0
        # find remaining colors that are shared, but don't have same index
        for i in range(0, (4 - black_feedback)):
            if guess[z] in code_copy:
                white_feedback += 1
                code_copy.remove(guess[z])
                guess.remove(guess[z])
                z -= 1
            z += 1
        return black_feedback, white_feedback
            
    def game_over_check(self):
        """ Process if game ends by running out of turns """
        if (self.player_wins == False) and (self.guesses_remaining == 0):
            self.game_over = True
        return self.game_over
    
### Test Code ###
if __name__ == "__main__":
    game = MasterMind()
    game.guess = ['pink', 'red', 'blue', 'pink']
    
    # Test win detection
    game.code = game.guess
    game.check_guess(game.guess, game.code)
    assert game.player_wins
    
    #new_game = Mastermind()
    game.code = ['red', 'red', 'red', 'red']
    game.new_guess = ['blue', 'blue', 'blue', 'blue']
    game.check_guess(game.new_guess, game.code)
    assert game.player_wins == False
    
    # check_guess upholds invariant
    try:
        game.guess = ['red', 'blue']
        game.check_guess(game.guess, game.code)
        assert False
    except:
        assert True
        
    # proper feedback return
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['red', 'blue', 'green', 'blue']
    assert game.give_feedback(game.guess) == (4, 0)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['yellow', 'blue', 'green', 'blue']
    assert game.give_feedback(game.guess) == (3, 0)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['yellow', 'yellow', 'green', 'blue']
    assert game.give_feedback(game.guess) == (2, 0)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['yellow', 'yellow', 'yellow', 'blue']
    assert game.give_feedback(game.guess) == (1, 0)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['yellow', 'yellow', 'yellow', 'yellow']
    assert game.give_feedback(game.guess) == (0, 0)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['blue', 'yellow', 'yellow', 'yellow']
    assert game.give_feedback(game.guess) == (0, 1)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['blue', 'green', 'yellow', 'yellow']
    assert game.give_feedback(game.guess) == (0, 2)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['blue', 'green', 'blue', 'yellow']
    assert game.give_feedback(game.guess) == (0, 3)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['blue', 'green', 'blue', 'red']
    assert game.give_feedback(game.guess) == (0, 4)
    
    game.guess = ['red', 'blue', 'green', 'blue']
    game.code = ['red', 'green', 'red', 'yellow']
    assert game.give_feedback(game.guess) == (1, 1)
    
    game.guess = ['red', 'yellow', 'green', 'blue']
    game.code = ['red', 'green', 'blue', 'pink']
    assert game.give_feedback(game.guess) == (1, 2)
    
    game.guess = ['red', 'yellow', 'green', 'blue']
    game.code = ['red', 'green', 'blue', 'yellow']
    assert game.give_feedback(game.guess) == (1, 3)
    
    game.guess = ['red', 'green', 'green', 'blue']
    game.code = ['red', 'green', 'blue', 'yellow']
    assert game.give_feedback(game.guess) == (2, 1)
    
    game.guess = ['red', 'green', 'yellow', 'blue']
    game.code = ['red', 'green', 'blue', 'yellow']
    assert game.give_feedback(game.guess) == (2, 2)