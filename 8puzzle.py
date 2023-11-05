import random
import copy

# Define the goal state for the 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, None]]

# Define the initial state
initial_state = [[1, None, 3],
                 [4, 2, 5],
                 [7, 8, 6]]

# Calculate the Manhattan distance heuristic
def h2(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] is not None:
                x, y = divmod(state[i][j] - 1, 3)  # Calculate the goal position
                distance += abs(i - x) + abs(j - y)
    return distance

# Define possible moves
def get_possible_moves(state):
    moves = []
    i, j = None, None  # Find the position of the blank tile
    for row in range(3):
        if None in state[row]:
            i, j = row, state[row].index(None)
            break
    if i > 0:
        moves.append((i - 1, j))  # Move the blank tile up
    if i < 2:
        moves.append((i + 1, j))  # Move the blank tile down
    if j > 0:
        moves.append((i, j - 1))  # Move the blank tile left
    if j < 2:
        moves.append((i, j + 1))  # Move the blank tile right
    return moves

# Hill-climbing search
def hill_climbing(initial_state):
    current_state = initial_state
    while True:
        # Calculate the heuristic value for the current state
        current_h2 = h2(current_state)

        # Check if the current state is the goal state
        if current_state == goal_state:
            return current_state

        # Generate possible successor states
        possible_moves = get_possible_moves(current_state)
        successors = []

        for move in possible_moves:
            successor_state = copy.deepcopy(current_state)
            i, j = move
            blank_i, blank_j = None, None  # Position of the blank tile
            for row in range(3):
                if None in successor_state[row]:
                    blank_i, blank_j = row, successor_state[row].index(None)
                    break
            successor_state[i][j], successor_state[blank_i][blank_j] = successor_state[blank_i][blank_j], successor_state[i][j]
            successors.append(successor_state)

        # Evaluate the successor states
        best_successor = min(successors, key=lambda state: h2(state))

        # Check if there's no better move
        if h2(best_successor) >= current_h2:
            return current_state

        # Move to the best successor state
        current_state = best_successor

# Solve the 8-puzzle
solution = hill_climbing(initial_state)
for row in solution:
    print(row)
