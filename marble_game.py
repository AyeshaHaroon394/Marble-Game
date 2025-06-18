import sys

class MarbleGame:
    def __init__(self, num_red, num_blue, version='standard', first_player='computer', depth=3):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth

    def game_over(self):
        if self.version == 'standard':
            return self.num_red == 0 or self.num_blue == 0
        elif self.version == 'misere':
            return self.num_red == 0 or self.num_blue == 0

    def get_score(self):
        return self.num_red * 2 + self.num_blue * 3

    def valid_move(self, red, blue):
        return 0 <= red <= self.num_red and 0 <= blue <= self.num_blue

    def make_move(self, red, blue):
        if self.valid_move(red, blue):
            self.num_red -= red
            self.num_blue -= blue

    def human_move(self):
        while True:
            red = int(input("Enter number of red marbles to take: "))
            blue = int(input("Enter number of blue marbles to take: "))
            if self.valid_move(red, blue):
                self.make_move(red, blue)
                break
            else:
                print("Invalid move. Try again.")

    def computer_move(self):
        move = self.minimax(self.num_red, self.num_blue, self.depth, -float('inf'), float('inf'), True)
        self.make_move(move[0], move[1])

    def minimax(self, red, blue, depth, alpha, beta, maximizing_player):
        if self.game_over() or depth == 0:
            return (None, None, self.get_score())

        if maximizing_player:
            max_eval = -float('inf')
            best_move = None
            for move in self.get_moves():
                self.make_move(*move)
                eval = self.minimax(self.num_red, self.num_blue, depth - 1, alpha, beta, False)[2]
                self.undo_move(*move)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return (*best_move, max_eval)
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_moves():
                self.make_move(*move)
                eval = self.minimax(self.num_red, self.num_blue, depth - 1, alpha, beta, True)[2]
                self.undo_move(*move)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return (*best_move, min_eval)

    def get_moves(self):
        if self.version == 'standard':
            return [(2, 0), (0, 2), (1, 0), (0, 1)]
        elif self.version == 'misere':
            return [(0, 1), (1, 0), (0, 2), (2, 0)]

    def undo_move(self, red, blue):
        self.num_red += red
        self.num_blue += blue

    def play(self):
        while not self.game_over():
            print(f"Red: {self.num_red}, Blue: {self.num_blue}")
            if self.current_player == 'human':
                self.human_move()
                self.current_player = 'computer'
            else:
                self.computer_move()
                self.current_player = 'human'
        print(f"Game Over! Final Score: {self.get_score()}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python marble_game.py <num-red> <num-blue> <version> <first-player> [depth]")
        sys.exit(1)

    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = sys.argv[3]
    first_player = sys.argv[4]
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else 3

    game = MarbleGame(num_red, num_blue, version, first_player, depth)
    game.play()
