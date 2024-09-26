class GameBoard:
    def __init__(self):
        self.spaces = [' '] * 9

    def show(self):
        for i in range(3):
            print(self.spaces[i*3], '|', self.spaces[i*3+1], '|', self.spaces[i*3+2])
            if i < 2:
                print('--+---+--')

    def place_marker(self, spot, marker):
        if self.spaces[spot] == ' ':
            self.spaces[spot] = marker
            return True
        return False

    def check_winner(self, marker):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for win in win_positions:
            if self.spaces[win[0]] == marker and self.spaces[win[1]] == marker and self.spaces[win[2]] == marker:
                return True
        return False

    def is_full(self):
        return ' ' not in self.spaces

class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.marker = None

    def pick_marker(self):
        while True:
            marker = input("Choose X or O? ").upper()
            if marker in ['X', 'O']:
                self.marker = marker
                break
            else:
                print("Please choose either X or O.")

    def move(self, board):
        while True:
            try:
                choice = int(input(f"{self.name}, pick a place(1-9): ")) - 1
                if 0 <= choice < 9:
                    if board.place_marker(choice, self.marker):
                        break
                    else:
                        print("This place is filled")
                else:
                    print("Choose a place between 1 and 9.")
            except ValueError:
                print("Enter a number.")

class TicTacToe:
    def __init__(self):
        self.board = GameBoard()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def start_game(self):
        self.player1.pick_marker()
        self.player2.marker = 'O' if self.player1.marker == 'X' else 'X'
        print(f"{self.player1.name} is {self.player1.marker}, {self.player2.name} is {self.player2.marker}.")

        current_player = self.player1
        while True:
            self.board.show()
            current_player.move(self.board)
            if self.board.check_winner(current_player.marker):
                self.board.show()
                print(f"{current_player.name} won")
                break
            elif self.board.is_full():
                self.board.show()
                print("Tie!")
                break
            current_player = self.player1 if current_player == self.player2 else self.player2

if __name__ == "__main__":
    ttt_game = TicTacToe()
    ttt_game.start_game()

