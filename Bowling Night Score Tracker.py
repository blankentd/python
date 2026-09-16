# Project: Bowling Night Score Tracker

""" This program simulates a bowling game for a group of friends. It generates random rolls for each player, calculates scores
based on standard bowling rules, and displays a scoreboard comparing everyone's performance.

Bowling scores are calculated based on the number of pins knocked down in each frame, with special scoring for strikes and spares.
For example, if a player rolls a strike (knocks down all 10 pins in the first roll of a frame), they receive 10 points plus the total 
of their next two rolls. If they roll a spare (knock down all 10 pins in two rolls of a frame), they receive 10 points plus the total
of their next roll. All other rolls are scored based on the number of pins knocked down. """

import random  # lets us use random.randint() to pick random numbers

def make_roller():
    # This list will hold every roll as it gets created, one at a time.
    # It starts empty because no balls have been bowled yet.
    generated_rolls = []

    # This is our "bookmark" -- it tracks how many rolls we've already
    # handed out to the main game loop below.
    index = 0

    # How many pins are standing right now, waiting to be knocked down.
    # A brand new frame always starts with all 10 pins up.
    pins_standing = 10

    # True if the next roll is the FIRST ball of a frame (fresh rack of pins).
    # False if the next roll is the SECOND ball (aiming at whatever pins are left).
    first_ball_of_frame = True

    def generate_next():
        # This function creates exactly one new roll and updates our
        # pin-tracking so the next roll knows how many pins are left.
        nonlocal pins_standing, first_ball_of_frame

        # Pick a random number of pins knocked down, but never more than
        # how many pins are actually still standing.
        roll = random.randint(0, pins_standing)

        # Save this roll so it's remembered for later.
        generated_rolls.append(roll)

        if first_ball_of_frame:
            # This roll was a first ball.
            if roll == 10:
                # Strike! All pins went down, so the frame is already over.
                # Next roll starts a brand new frame with a full rack.
                pins_standing = 10
                first_ball_of_frame = True
            else:
                # Not a strike -- some pins are still standing.
                # The next roll (second ball) can only hit what's left.
                pins_standing -= roll
                first_ball_of_frame = False
        else:
            # This roll was a second ball, so the frame is over no matter
            # what happened. Reset everything for the next frame.
            pins_standing = 10
            first_ball_of_frame = True

    def upcoming(n=1, consume=True):
        # This is how the main game loop asks for roll values.
        # n = how many rolls to fetch (1 normally, 2 for some bonus checks)
        # consume = should this move the bookmark forward?
        #   True  -> these rolls belong to the current frame for real
        #   False -> we're just "peeking" ahead to calculate a bonus,
        #            without using these rolls up yet
        nonlocal index

        # If we don't have enough rolls generated yet to answer this
        # request, make more rolls until we do.
        while len(generated_rolls) < index + n:
            generate_next()

        # Grab the rolls we need, starting from our bookmark.
        values = generated_rolls[index:index + n]

        if consume:
            # Move the bookmark forward so these rolls aren't reused.
            index += n

        if n == 1:
            # If only 1 roll was asked for, just return that single number
            # instead of a list containing one number.
            return values[0]
        return values

    # Hand back the "upcoming" function so the game loop can call it
    # over and over to get roll values.
    return upcoming


Players = ["Tom"]  # list of players -- add more names here later

for n in Players:
    totalScore = 0          # this player's running score starts at 0
    upcoming = make_roller()  # set up a fresh roll generator for this player

    for i in range(10):  # bowling has 10 frames, i goes from 0 to 9
        if i < 9:
            # ----- Frames 1 through 9: normal rules -----

            first = upcoming()  # get the first ball of this frame

            if first == 10:  # Strike (knocked down all 10 on the first ball)
                # A strike's bonus is "whatever the next 2 balls score."
                # We PEEK at them (consume=False) because those same balls
                # will be bowled for real when the next frame runs.
                bonus = sum(upcoming(2, consume=False))
                totalScore += first + bonus
                print(f"Frame {i + 1}: {n} rolled a strike")

            else:
                # Not a strike, so we need a real second ball.
                second = upcoming()
                frame_total = first + second

                if frame_total == 10:  # Spare (both balls together = 10)
                    # A spare's bonus is just the next 1 ball, also peeked.
                    bonus = upcoming(1, consume=False)
                    totalScore += frame_total + bonus
                    print(f"Frame {i + 1}: {n} rolled a spare")
                else:
                    # Open frame -- no bonus, just add up the two balls.
                    totalScore += frame_total
                    print(f"Frame {i + 1}: {n} rolled {first}, then {second}")

        else:
            # ----- Frame 10: special rules -----
            # There's no "next frame" to borrow bonus balls from, so any
            # bonus balls here are bowled for real, right in this frame.

            first = upcoming()

            if first == 10:  # Strike
                # Get 2 more real balls as the bonus (up to 3 balls total).
                second, third = upcoming(2)
                totalScore += first + second + third
                print(f"Frame {i + 1}: {n} rolled a strike, bonus rolls {second} and {third}")

            else:
                second = upcoming()
                frame_total = first + second

                if frame_total == 10:  # Spare
                    # Get 1 more real ball as the bonus (3 balls total).
                    third = upcoming()
                    totalScore += frame_total + third
                    print(f"Frame {i + 1}: {n} rolled a spare, bonus roll {third}")
                else:
                    # Open frame -- just 2 balls, no bonus.
                    totalScore += frame_total
                    print(f"Frame {i + 1}: {n} rolled {first}, then {second}")

    # All 10 frames are done -- show this player's final score.
    print(f"{n}'s score: {totalScore}")