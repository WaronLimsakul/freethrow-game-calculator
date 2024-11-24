import numpy as np
import sys

a_fg = float(sys.argv[1])
b_fg = float(sys.argv[2])
goal = float(sys.argv[3])
if len(sys.argv) == 5:
    simulations = sys.argv[4]
else:
    simulations = 100000


def one_turn(prob, goal):  # simulate one turn
    scores = 0
    shots = 0
    while scores < goal:
        shots += 1
        if np.random.rand() < prob:
            scores += 1
    return shots


a_games = 0
b_games = 0
tie_games = 0


def one_turn_game(a_fg, b_fg, goal):  # simulate one game
    a_shots = one_turn(a_fg, goal)
    b_shots = one_turn(b_fg, goal)
    if a_shots < b_shots:
        return "A"
    elif a_shots == b_shots:
        return "Tie"
    else:
        return "B"


# run simulations
for _ in range(simulations):
    result = one_turn_game(a_fg, b_fg, goal)
    if result == "A":
        a_games += 1
    elif result == "Tie":
        tie_games += 1
    else:
        b_games += 1
print(f"a winning chance: {a_games * 100 / simulations}%")
print(f"b winning chance: {b_games * 100 / simulations}%")
print(f"tie chance: {tie_games * 100 / simulations}%")
