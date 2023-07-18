import math
import os
import time
class firstWon():
    def __init__(self, curr_moves):
        self.curr_moves = curr_moves
    
    def state(self):
        if ((self.curr_moves[0] == 'x' and self.curr_moves[1] == 'x' and self.curr_moves[2] == 'x') or
            (self.curr_moves[3] == 'x' and self.curr_moves[4] == 'x' and self.curr_moves[5] == 'x') or
            (self.curr_moves[6] == 'x' and self.curr_moves[7] == 'x' and self.curr_moves[8] == 'x') or
            (self.curr_moves[0] == 'x' and self.curr_moves[3] == 'x' and self.curr_moves[6] == 'x') or
            (self.curr_moves[1] == 'x' and self.curr_moves[4] == 'x' and self.curr_moves[7] == 'x') or
            (self.curr_moves[2] == 'x' and self.curr_moves[5] == 'x' and self.curr_moves[8] == 'x') or 
            (self.curr_moves[0] == 'x' and self.curr_moves[4] == 'x' and self.curr_moves[8] == 'x') or
            (self.curr_moves[2] == 'x' and self.curr_moves[4] == 'x' and self.curr_moves[6] == 'x')):
            return True
        else: return False
    
    def tie(self):
        self.not_first_time = False
        count = 0
        for val in self.curr_moves:
            if (isinstance(self.val,int) != True and self.not_first_time):
                self.count = self.count+1
        if (self.count == 9):
            return True
        self.not_first_time = True
        return False

class secondWon():
    def __init__(self, curr_moves):
        self.curr_moves = curr_moves
    def state(self):
        if ((self.curr_moves[0] == 'o' and self.curr_moves[1] == 'o' and self.curr_moves[2] == 'o') or
            (self.curr_moves[3] == 'o' and self.curr_moves[4] == 'o' and self.curr_moves[5] == 'o') or
            (self.curr_moves[6] == 'o' and self.curr_moves[7] == 'o' and self.curr_moves[8] == 'o') or
            (self.curr_moves[0] == 'o' and self.curr_moves[3] == 'o' and self.curr_moves[6] == 'o') or
            (self.curr_moves[1] == 'o' and self.curr_moves[4] == 'o' and self.curr_moves[7] == 'o') or
            (self.curr_moves[2] == 'o' and self.curr_moves[5] == 'o' and self.curr_moves[8] == 'o') or 
            (self.curr_moves[0] == 'o' and self.curr_moves[4] == 'o' and self.curr_moves[8] == 'o') or
            (self.curr_moves[2] == 'o' and self.curr_moves[4] == 'o' and self.curr_moves[6] == 'o')):
            return True
        else: return False

class board():
    def __init__(self, curr_moves):
        self.curr_moves = curr_moves
    def curr(self):
        return f"""
    -------------------------------------------------
    |               |               |               |
    |\t    {self.curr_moves[0]}\t    |\t    {self.curr_moves[1]}\t    |\t    {self.curr_moves[2]}\t    | 
    |_______________|_______________|_______________|
    |               |               |               |
    |\t    {self.curr_moves[3]}\t    |\t    {self.curr_moves[4]}\t    |\t    {self.curr_moves[5]}\t    |
    |_______________|_______________|_______________|
    |               |               |               |
    |\t    {self.curr_moves[6]}\t    |\t    {self.curr_moves[7]}\t    |\t    {self.curr_moves[8]}\t    | 
    |               |               |               |
    -------------------------------------------------"""

class player_move(): 
    def __init__(self, curr_moves, player,player_symbol):
        self.curr_moves = curr_moves
        self.player = player
        self.player_symbol = player_symbol
    def action(self):
        self.user_choice = input(f"{self.player} please select a number from the board: ")
        while (self.user_choice.strip().isdigit() == False or int(self.user_choice) not in self.curr_moves):
            print ("Invalid! Enter Again!")
            self.user_choice = input(f"{self.player} please select a number from the board: ")
        self.curr_moves[int(self.user_choice)-1] = self.player_symbol
        os.system('cls')
        print(board(self.curr_moves).curr())

class game():
    def __init__(self):
        self.name = "Jun"
        self.array_moves = [1,2,3,4,5,6,7,8,9]
        self.first_player = input("First player enter your name: ")
        self.second_player = input("Second player enter your name: ")
        os.system('cls')
        print(f"{self.first_player} you are x!\n{self.second_player} you are o!")
        time.sleep(5)
        os.system('cls')
        print(board(self.array_moves).curr())

        while (firstWon(self.array_moves).state() == False and secondWon(self.array_moves).state() == False and firstWon(self.array_moves).tie() == False):
            player_move(self.array_moves,self.first_player,'x').action()
            if (firstWon(self.array_moves).state() == False and firstWon(self.array_moves).tie() == False):
                player_move(self.array_moves,self.second_player,'o').action()
        if (firstWon(self.array_moves).state() == True):
            print(f"{self.first_player} won!")
        elif(firstWon(self.array_moves).tie() == True):
            print("It's a tie!!!")
        else:
            print(f"{self.second_player} won!")

def main():
    should_exit = False
    while (not should_exit):
        game()
        playAgain = None
        while (playAgain != "Y" and playAgain != "N"):
            playAgain = input("Would you like to play again? (Y or N): ")
        if (playAgain == "N"):
            should_exit = True


    # playAgain = None
    # while (playAgain != "Y" and playAgain != "N"):
    #     playAgain = input("Would you like to play again? (Y or N): ")
    # if (playAgain == "Y"):
    #     os.system('cls')
    #     game()
    # else:
    #     exit()

if __name__ == "__main__":
    main()

    
    




