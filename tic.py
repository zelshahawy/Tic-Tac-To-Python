import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        '''
        input None
        edits board to have a 3 x 3 array
        outputs None
        '''
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
        return None

    def get_random_first_player(self):
        '''
        input None
        returns 0 or 1 randomly to choose players
        '''
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        '''
        Input:
        Row: Int representing a row of the array Board
        Col: int representing a column of the array board
        Player: either X or O

        Output: overwrites a free space into the letter designating a player
        '''
        self.board[row][col] = player

    def is_player_win(self, player):
        '''
        Checks if a player has won the game
        '''
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        '''
        checks if a board has been completely filled thus ending the game
        '''
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_spot_taken(self, spot):
        '''
        Checks if a spot is already taken by a player
        '''
        if spot == '-':
            return False
        else:
            return True

    def start(self):
        while True:
            self.create_board()
            if self.get_random_first_player() == 1:
                player = 'X'
            else:
                player = 'O'
            while True:
                print(f"Player {player} turn")

                self.show_board()
                flag = False
                while True:
                    try:
                        row, col = list(
                            map(int, input("Enter row and column numbers to\
                                fix spot: ").split()))
                        while self.is_spot_taken(self.board[row - 1][col - 1]):
                            self.show_board()
                            row, col = list(
                                map(int, input(print("You inputted an already\
                                    taken spot, Choose again:\n ")).split()))
                        break
                    except ValueError:
                        print()
                        print('You have typed an invalid value. Please try\
                            again')
                        self.show_board()
                print()
                self.fix_spot(row - 1, col - 1, player)
                if self.is_player_win(player):
                    print(f"Player {player} wins the game!")
                    break
                if self.is_board_filled():
                    print("Match Draw!")
                    break
                player = self.swap_player_turn(player)
            print()
            self.show_board()
            choice = input("Wanna play again? Y/N")
            if choice == 'N':
                break
            else:
                self.create_board()



# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
