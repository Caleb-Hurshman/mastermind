"""
Purpose: Create a GUI of a mastermind board with guess-making functionality
Assignment: CS 108 Final Project
Author: Caleb Hurshman (cah222)
"""

from tkinter import *
from tkinter import messagebox
from game import *

class GUI:
    """ Create a mastermind board """
    def __init__(self, window, end_game):
        self.window = window
        self.width = 500
        self.game = MasterMind()
        self.master_code = self.game.create_code()
        #print(self.master_code)   #Testing purposes
        self.temp_guesses = 0
        self.end_game = end_game
        self.result = True
        
        
        self.canvas = Canvas(self.window, bg='white', width=self.width, height=self.width)
        self.canvas.pack()
        self.canvas.create_text(75, 25, text='Guesses Left: ' + str(self.game.guesses_remaining), tag='guess_remaining_text')
        
        red_button = Button(window, text = 'Red', bg='red', padx=20, command=self.red_guess)
        red_button.pack(side = LEFT)
        
        blue_button = Button(window, text = 'Blue', bg='blue', padx=20, command=self.blue_guess)
        blue_button.pack(side = LEFT)
        
        green_button = Button(window, text = 'Green', bg='green', padx=20, command=self.green_guess)
        green_button.pack(side = LEFT)
        
        yellow_button = Button(window, text = 'Yellow', bg='yellow', padx=20, command=self.yellow_guess)
        yellow_button.pack(side = LEFT)
        
        orange_button = Button(window, text = 'Orange', bg='darkorange', padx=20, command=self.orange_guess)
        orange_button.pack(side = LEFT)
        
        pink_button = Button(window, text = 'Pink', bg='pink', padx=20, command=self.pink_guess)
        pink_button.pack(side = LEFT)
        
        delete_button = Button(window, text = 'Delete', padx=28, command=self.delete_last_guess)
        delete_button.pack()
        
        guess_button = Button(window, text = 'Enter Guess', pady=10, command=self.save_guess)
        guess_button.pack()
        
        rules_button = Button(window, text = 'Game Rules', command=self.show_rules)
        rules_button.pack()
        
        self.guess = []
        self.draw_board()
        
    def draw_board(self):
        linex = 100
        for i in range(5):
            self.canvas.create_line(linex, 75, linex, 475)
            linex += 60
        liney = 75
        for i in range(11):
            self.canvas.create_line(100, liney, 340, liney)
            liney += 40
        linex = 370
        for i in range(3):
            self.canvas.create_line(linex, 75, linex, 475)
            linex += 30
        liney = 75
        for i in range(21):
            self.canvas.create_line(370, liney, 430, liney)
            liney += 20
            
    """ next 6 methods detect if a color button is pressed and save the color in the guess,
    only if there are less than 4 guess colors in the temporary sequence """
    def red_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('red')
            self.draw_guess('red')
            self.temp_guesses += 1
        
    def blue_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('blue')
            self.draw_guess('blue')
            self.temp_guesses += 1
        
    def green_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('green')
            self.draw_guess('green')
            self.temp_guesses += 1
        
    def yellow_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('yellow')
            self.draw_guess('yellow')
            self.temp_guesses += 1
        
    def orange_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('orange')
            self.draw_guess('orange')
            self.temp_guesses += 1
        
    def pink_guess(self):
        if self.temp_guesses < 4:
            self.guess.append('pink')
            self.draw_guess('pink')
            self.temp_guesses += 1
        
    def delete_last_guess(self):
        """ Remove guess from current sequence and erase the corresponding oval on the canvas, only if there is one to delete """
        if self.temp_guesses > 0:
            self.canvas.delete('guess_' + str(len(self.guess) - 1) + str(self.game.guesses_remaining))
            del self.guess[-1]
            self.temp_guesses -= 1
            
    def show_rules(self):
        basic_rules = """The Mastermind has created a 4-color code using 6 different color possibilities.\n
Your job is to guess the code. After each guess, the Mastermind will give you feedback.\n
A black feeback pin means one of your colors is the same color and position as the Master Code\n
A white feedback pin means you have the right color in one of your slots, but it isn't in the right spot\n
You have 10 guesses to figure out the Master Code\n
For any clarification, ask Caleb Hurshman, the Mastermind behind this Mastermind"""
        messagebox.showinfo("Mastermind Rules", basic_rules)
              
    def draw_guess(self, color):
        """ Iterate through guess and draw colored oval with color matching the guess color, positioned based on turn and index """
        if (self.game.game_over == False) and (self.game.player_wins == False):
            self.y_coord = (self.game.guesses_remaining * 40) + 45
            for index, color in enumerate(self.guess):
                self.x_coord = (index * 60) + 120
                self.index = str(index)
                self.canvas.create_oval(self.x_coord, self.y_coord, (self.x_coord + 20), (self.y_coord + 20), fill=color, tag=self.create_tag())
            
    def create_tag(self):
        """ Create a unique tag for each colored guess oval drawn to the board """
        column = self.index
        row = str(self.game.guesses_remaining)
        tag = 'guess_' + column + row
        return tag

    def save_guess(self):
        """ Call for feedback, reset guess list, update guess remaining text"""
        if (self.game.game_over == False) and (self.game.player_wins == False):
            try:
                # delete previous error messages
                self.canvas.delete('guess_length_error')
                self.game.check_guess(self.guess, self.master_code)
                
                # get/draw feedback
                self.guess_feedback = self.game.give_feedback(self.guess)
                self.draw_feedback()
                
                # update guess remaining text
                self.canvas.delete('guess_remaining_text')
                self.game.guesses_remaining -= 1
                self.canvas.create_text(75, 25, text='Guesses Left: ' + str(self.game.guesses_remaining), tag='guess_remaining_text')
                
                # check if player guessed correctly or lost by running out of turns
                if self.game.player_wins:
                    self.display_game_over('W', self.canvas)
                self.game.game_over_check()
                if self.game.game_over:
                    self.display_game_over('L', self.canvas)
                
                # reset guess list and temp guess count 
                self.guess = []
                self.temp_guesses = 0
            except IndexError:
                self.canvas.create_text(128, 45, text='Must have 4 colors in the guess', tag='guess_length_error')
        
    def draw_feedback(self):
        """ Draw black and white feedback circles on right of guess """
        black_ovals = self.guess_feedback[0]
        white_ovals = self.guess_feedback[1]
        self.feedback_counter = 0
        self.fb_y = (self.game.guesses_remaining * 40) + 60
        for i in range(0, (black_ovals + white_ovals)):
            if i < black_ovals:
                fill_color = 'black'
            else:
                fill_color = 'white'
            self.feedback_coord()
            self.canvas.create_oval(self.fb_x, self.fb_y, (self.fb_x + 10), (self.fb_y + 10), fill=fill_color)
            self.feedback_counter += 1
            
    def feedback_coord(self):
        """ Determine the coordinates for a feedback pin"""
        if (self.feedback_counter % 2) == 0:
            self.fb_x = 380
        else:
            self.fb_x = 410
        if self.feedback_counter == 2:
            self.fb_y -= 20
        return self.fb_x, self.fb_y
            
    def display_game_over(self, result, canvas):
        """ Print a message to tell user the game is over, display the master code if user lost"""
        if result == 'W':
            self.canvas.create_text(250, 50, text="CONGRATS, YOU WON!")
        elif result == 'L':
            self.canvas.create_text(250, 25, text="You lost, better luck next time.")
            self.canvas.create_text(250, 50, text="The code was: ", anchor=E)
            endx = 255
            for i in range(len(self.master_code)):
                self.canvas.create_oval(endx, 40, (endx + 20), 60, fill=self.master_code[i])
                endx += 30
            
                         
### Test Code ###
if __name__ == '__main__':
    root = Tk()
    root.title('Mastermind')
    end_game = False
    app = GUI(root, end_game)
    root.mainloop()
