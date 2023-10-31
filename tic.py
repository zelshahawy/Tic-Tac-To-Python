import random


class TicTacToe:
    '''
    Initializes a new instance of the TicTacToe class.
    '''
    def __init__(self):
        """
        Initializes an empty game board.
        """
        self.board = []

    def create_board(self):
        '''
        input None
        Creates an empty 3x3 game board, resetting the game state.
        Returns None
        '''
        self.board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append('-')
            self.board.append(row)
        return None

    def get_random_first_player(self):
        '''
        Randomly selects the first player ('X' or 'O') to start the game.
        input None
        Returns:
        int: 0 for 'X' and 1 for 'O'.
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
        Checks if the specified player has won the game.

        Inputs:
        player (str): The player's mark ('X' or 'O') to check for a win.

        Returns:
        bool: True if the player has won, False otherwise.
        '''
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
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        '''
        Checks if the game board is completely filled, leading to a draw.
        
        Input None
        
        Returns:
        bool: True if the board is filled, False otherwise.
        '''
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        """
        Swaps the player's turn between 'X' and 'O'.

        Input:
        player (str): The current player's mark ('X' or 'O').

        Returns:
        str: The next player's mark ('X' or 'O').
        """
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        """
        Displays the current game board in the console
        """
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_spot_taken(self, spot):
        """
        Checks if a spot on the game board is already taken by a player's mark.

        Input:
        spot (str): The mark at a specific spot on the game board.

        Returns:
        bool: True if the spot is taken, False if it's empty ('-').
        """
        if spot == '-':
            return False
        else:
            return True

    def start(self):
        """
        Starts the Tic-Tac-Toe game and manages the game flow.
        """
        print("Welcome to Tic Tac Toe Game!")
        print("Type 'exit' to exit the game")
        flag = True
        while flag:
            self.create_board()
            if self.get_random_first_player() == 1:
                player = 'X'
            else:
                player = 'O'
            while True:
                print(f"Player {player} turn")
                self.show_board()
                while True:
                    try:
                        row_col = input("Enter row and column numbers to fix spot (or 'exit' to quit): ").strip()
                        if row_col == "exit":
                            flag = False
                            break
                        row, col = list(map(int, row_col.split()))
                        while self.is_spot_taken(self.board[row - 1][col - 1]):
                            self.show_board()
                            row_col = input("You inputted an already taken spot, Choose again (or 'exit' to quit):\n ").strip()
                            if row_col == "exit":
                                flag = False
                                break
                            row, col = list(map(int, row_col.split()))
                        if row_col == "exit":
                            flag = False
                            break
                        break
                    except ValueError:
                        print()
                        print('You have typed an invalid value. Please try again')
                        self.show_board()
                    except IndexError:
                        print()
                        print('You have entered an invalid index. Please try again')
                        self.show_board()
                if not flag:
                    break
                print()
                self.fix_spot(row - 1, col - 1, player)
                if self.is_player_win(player):
                    print(f"Player {player} wins the game!")
                    break
                if self.is_board_filled():
                    print("Match Draw!")
                    break
                player = self.swap_player_turn(player)
            if not flag:
                break
            print()
            self.show_board()
            choice = input("Wanna play again? Y/N").lower()
            if choice == 'n':
                break
            else:
                self.create_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
