import numpy as np
import sys

a_fg = float(sys.argv[1])  # first argument is first player's scoring probability
b_fg = float(sys.argv[2])  # secodn argument is second player's scoring probability
goal = int(sys.argv[3])  # how many shot it takes to win.
if len(sys.argv) == 5:
    # you set put how many times you want to simulate (auto 100000 times)
    simulations = int(sys.argv[4])
else:
    simulations = 100000


# function for simulate one game.
def simulate_game(a_fg, b_fg, goal):
    a = b = 0
    turn_a = True

    while a < goal and b < goal:
        if turn_a:
            if np.random.rand() < a_fg:
                a += 1
        else:
            if np.random.rand() < b_fg:
                b += 1
        turn_a = not turn_a

    if a == goal:
        return "A"
    else:
        return "B"


a_count = b_count = 0


# iterate each game
for _ in range(simulations):
    if simulate_game(a_fg, b_fg, goal) == "A":
        a_count += 1
    else:
        b_count += 1

print(f"a winning chance: {a_count * 100 / simulations}%")
print(f"b winning chance: {b_count * 100 / simulations}%")
