# Project: Bowling Night Score Tracker

""" This program simulates a bowling game for a group of friends. It generates random rolls for each player, calculates scores
based on standard bowling rules, and displays a scoreboard comparing everyone's performance.

Bowling scores are calculated based on the number of pins knocked down in each frame, with special scoring for strikes and spares.
For example, if a player rolls a strike (knocks down all 10 pins in the first roll of a frame), they receive 10 points plus the total 
of their next two rolls. If they roll a spare (knock down all 10 pins in two rolls of a frame), they receive 10 points plus the total
of their next roll. All other rolls are scored based on the number of pins knocked down. """

import random

""" 
score = 0
totalScore = 0

Players = ["Tom", "Sally", "Juan", "Stella"]

for n in Players:
    for i in range(10):
        score = random.randint(0, 10)
        totalScore += score
    print(f"{n}'s score: {totalScore}")

"""

import random

def make_roller(rolls):
    index = 0
    def upcoming(n=1, consume=True):
        nonlocal index
        values = rolls[index:index + n]
        if consume:
            index += n
        if n == 1:
            return values[0] if values else 0
        return values
    return upcoming

Players = ["Tom"]

for n in Players:
    totalScore = 0
    rolls = [random.randint(0, 10) for _ in range(21)]
    upcoming = make_roller(rolls)

    for i in range(10):
        if i < 9:
            # Frames 1-9: normal rules, bonus rolls are peeked, not consumed
            first = upcoming()
            if first == 10:  # Strike
                bonus = sum(upcoming(2, consume=False))
                totalScore += first + bonus
                print(f"Frame {i + 1}: {n} rolled a strike")
            else:
                second = upcoming()
                frame_total = first + second
                if frame_total == 10:  # Spare
                    bonus = upcoming(1, consume=False)
                    totalScore += frame_total + bonus
                    print(f"Frame {i + 1}: {n} rolled a spare")
                else:
                    totalScore += frame_total
                    print(f"Frame {i + 1}: {n} rolled {first}, then {second}")
        else:
            # Frame 10: special rules, all bonus rolls are real and consumed
            first = upcoming()
            if first == 10:  # Strike
                second, third = upcoming(2)
                totalScore += first + second + third
                print(f"Frame {i + 1}: {n} rolled a strike, bonus rolls {second} and {third}")
            else:
                second = upcoming()
                frame_total = first + second
                if frame_total == 10:  # Spare
                    third = upcoming()
                    totalScore += frame_total + third
                    print(f"Frame {i + 1}: {n} rolled a spare, bonus roll {third}")
                else:
                    totalScore += frame_total
                    print(f"Frame {i + 1}: {n} rolled {first}, then {second}")

    print(f"{n}'s score: {totalScore}")