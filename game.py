import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer



class TicTacToe:
    def __init__(self):
        self.board = self.make_board() #we will use a single list to rep 3x3 board
        self.current_winner = None #keep track of winner!

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i  in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

        
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to checknall of these!
        # first let's check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        #print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        #print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            #print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
            return False       
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') #just Empty Line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter    

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' #Switching players
            # if letter == 'X':
            #    letter = 'O'
            #else:
            #    letter = 'X'
        time.sleep(.8)
            # BUT WAIT WHAT IF WE WANT?
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)