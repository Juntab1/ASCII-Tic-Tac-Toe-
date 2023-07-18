import os
import time

# keeps track of if someone has 3 in a row to win or not
class whoWon():
    def __init__(self, curr_moves, player_symbol):
        self.curr_moves = curr_moves
        self.player_symbol = player_symbol
    
    def state(self):
        if ((self.curr_moves[0] == self.player_symbol and self.curr_moves[1] == self.player_symbol and self.curr_moves[2] == self.player_symbol) or
            (self.curr_moves[3] == self.player_symbol and self.curr_moves[4] == self.player_symbol and self.curr_moves[5] == self.player_symbol) or
            (self.curr_moves[6] == self.player_symbol and self.curr_moves[7] == self.player_symbol and self.curr_moves[8] == self.player_symbol) or
            (self.curr_moves[0] == self.player_symbol and self.curr_moves[3] == self.player_symbol and self.curr_moves[6] == self.player_symbol) or
            (self.curr_moves[1] == self.player_symbol and self.curr_moves[4] == self.player_symbol and self.curr_moves[7] == self.player_symbol) or
            (self.curr_moves[2] == self.player_symbol and self.curr_moves[5] == self.player_symbol and self.curr_moves[8] == self.player_symbol) or 
            (self.curr_moves[0] == self.player_symbol and self.curr_moves[4] == self.player_symbol and self.curr_moves[8] == self.player_symbol) or
            (self.curr_moves[2] == self.player_symbol and self.curr_moves[4] == self.player_symbol and self.curr_moves[6] == self.player_symbol)):
            return True
        else: return False

# game board
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

# asks the users for their move and updates the game board
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

# overall operation of what happens when the user runs the game is covered here from start to finish
class game():
    def __init__(self):
        self.array_moves = [1,2,3,4,5,6,7,8,9]
        self.first_player = input("First player enter your name: ")
        self.second_player = input("Second player enter your name: ")
        os.system('cls')
        print(f"{self.first_player} you are x!\n{self.second_player} you are o!")
        time.sleep(3)
        os.system('cls')
        print(board(self.array_moves).curr())
        self.count = 0
        while (whoWon(self.array_moves,'x').state() == False and whoWon(self.array_moves, 'o').state() == False and self.count < 9):
            player_move(self.array_moves,self.first_player,'x').action()
            self.count = self.count+1
            if (whoWon(self.array_moves, 'x').state() == False and self.count < 9):
                player_move(self.array_moves,self.second_player,'o').action()
                self.count = self.count+1
        if (whoWon(self.array_moves,'x').state() == True):
            print(f"{self.first_player} won!")
        elif(self.count >= 9):
            print("It's a tie!!!")
        else:
            print(f"{self.second_player} won!")

# checks if the user wants to play the game again or not
def main():
    should_exit = False
    while (not should_exit):
        os.system('cls')
        game()
        playAgain = "A"
        while (playAgain.strip() != "Y" and playAgain.strip() != "N"):
            playAgain = input("Would you like to play again? (Y or N): ")
        if (playAgain.strip() == "N"):
            should_exit = True

if __name__ == "__main__":
    main()

    
    




