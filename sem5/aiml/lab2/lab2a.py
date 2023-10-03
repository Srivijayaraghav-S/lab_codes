import random
import math
# 1. Generate a random initial board
def random_board(n=8):
    """Generate a random board of size n x n"""
    return [random.randint(0, n-1) for _ in range(n)]
# 2. Calculate the cost (number of pairwise attacks)
def cost(board):
    """Compute the number of pairwise attacks for the board"""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j]:  # Same row
                attacks += 1
            if abs(board[i] - board[j]) == j - i:  # Diagonal
                attacks += 1 
    return attacks
# 3. Generate neighboring boards
def neighbors(board):
    """Generate all possible neighbors of the board by moving a single queen to a different row in its column"""
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i] != j:
                new_board = list(board)
                new_board[i] = j
                yield new_board
# 4. Simulated Annealing
def simulated_annealing(initial_board, temperature, cooling_rate, max_steps):
    """Perform the simulated annealing algorithm to find a solution to the n-queens problem"""
    current_board = initial_board
    current_cost = cost(current_board)
    for step in range(max_steps):
        T = temperature * (cooling_rate ** step)
        if T <= 0 or current_cost == 0:
            return current_board
        next_board = random.choice(list(neighbors(current_board)))
        next_cost = cost(next_board)
        delta_cost = next_cost - current_cost
        if delta_cost < 0 or random.random() < math.exp(-delta_cost / T):
            current_board, current_cost = next_board, next_cost
    return current_board
# Run simulated annealing to find a solution for the 8-queens problem
initial_board = random_board()
solution = simulated_annealing(initial_board, temperature=10, cooling_rate=0.995, max_steps=10000)
print(solution, cost(solution))
#Output
([3, 1, 7, 4, 6, 0, 2, 5], 0)