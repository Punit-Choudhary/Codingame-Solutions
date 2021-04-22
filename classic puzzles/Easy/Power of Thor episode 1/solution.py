"""
# ****************************************** #
# Codingame.com solutions by Punit-Choudhary #
# ****************************************** #
#                                            #
# Puzzle: Power of Thore Episode 1           #
# Difficulty: Easy                           #
# Topic: Conditions                          #
#                                            #
# ****************************************** #
"""

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    if light_y == initial_ty:
        if light_x > initial_tx:
            print("E")
            initial_tx += 1
        else:
            print("W")
            initial_tx -= 1
    elif light_x == initial_tx:
        if light_y > initial_ty:
            print("S")
            initial_ty -= 1
        else:
            print("N")
            initial_ty += 1
    elif light_x < initial_tx:
        if light_y < initial_ty:
            print("NW")
            initial_tx -= 1
            initial_ty -= 1
        else:
            print("SW")
            initial_tx -= 1
            initial_ty += 1
    else:
        if light_y < initial_ty:
            print("NE")
            initial_tx += 1
            initial_ty -= 1
        else:
            print("SE")
            initial_tx += 1
            initial_ty += 1
