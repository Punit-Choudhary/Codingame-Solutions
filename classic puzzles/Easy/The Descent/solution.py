import sys

while True:
    value = 0
    largest = 0

    for i in range(8):
        mountain_h = int(input())

        if mountain_h > largest:
            largest = mountain_h
            value = i
    print(value)
