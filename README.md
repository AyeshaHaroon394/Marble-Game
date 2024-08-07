# DEP

--Command Line
3.1 Usage
To start the game, use the following command-line invocation:
python marble_game.py <num-red> <num-blue> <version> <first-player>

--Turn Order
4.1 Turn Order
The game alternates between the human and computer player until the game ends.
4.2 Human Move
The program prompts the human player for their move and validates the input.
4.3 Computer Move
The program determines the computer's move using the MinMax algorithm with Alpha Beta Pruning.

--MinMax Algorithm
5.1 Overview
The MinMax algorithm is used to optimize decision-making in the game by evaluating possible moves and selecting the best one.
5.2 Alpha Beta Pruning
Alpha Beta Pruning is a technique used to improve the efficiency of the MinMax algorithm by eliminating branches that cannot influence the final decision.
5.3 Move Ordering (Standard)
Pick 2 red marbles.
Pick 2 blue marbles.
Pick 1 red marble.
Pick 1 blue marble.
5.4 Move Ordering (Misère)
Pick 1 blue marble.
Pick 1 red marble.
Pick 2 blue marbles.
Pick 2 red marbles.

--End of Game
7.1 Game Over Conditions
The game ends when either pile is empty.
7.2 Scoring Calculation
The final score is calculated based on the remaining marbles: red marbles are worth 2 points each, and blue marbles are worth 3 points each.

--Implementation Details
8.1 Modules
Command-line parsing: Handles input from the command line.
Game mechanics: Manages the state of the game, including the number of marbles and turn order.
Human and computer moves: Handles the moves made by the human and computer players.
AI decision-making with MinMax and Alpha Beta Pruning: Implements the AI logic for determining the best move.
