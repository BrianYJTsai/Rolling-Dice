#  File: Dice.py
#  Description: Program simulates the roll of two dice. Input is the number of dice rolls.
#  Output is the histogram of the outcomes.
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 9/9/17
#  Date Last Modified: 9/9/17

import random

def generateRolls(numDiceRolls):

    # Initialize all possible dice outcomes to 0
    dictDiceRolls = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    # Randomly generate values for all possible dice outcomes
    for roll in range(0, numDiceRolls):
        randomRoll = random.randint(1, 6) + random.randint(1, 6)
        dictDiceRolls[randomRoll] += 1

    return dictDiceRolls

def generateDiceList(dictDiceRolls):

    # Initialize a new list
    listDiceRolls = []

    # Append all dictionary values into the list
    for roll in range(2, 13):
        listDiceRolls.append(dictDiceRolls[roll])

    return listDiceRolls

def drawVerticalAxis(dictDiceRolls, numDiceRolls):

    # Set the scale factor
    # If the number of trials is less than or equal to 100, then there is no need to scale the outcomes
    if (numDiceRolls <= 100):
        denominator = 100
    # If the number of trials is greater than 100, then scale the outcomes as: outcome * (100/trials)
    else:
        denominator = numDiceRolls

    # Find the maximum number of rows in the histogram
    max = 0
    for index in range(2, 13):
        if (max < dictDiceRolls[index]):
            max = dictDiceRolls[index]

    # Scale the maximum if necessary
    if (numDiceRolls > 100):
        max = round(max * 100 / numDiceRolls)

    # Iterate over the max number of pipes to draw, counting down
    for row in range(max, 0, -1):
        print("|", end = "")

        # Iterate over the number of possible outcomes, scale the outcome if necessary
        for column in range(2, 13):

            # Draw an asterisk if necessary
            if (round(dictDiceRolls[column] * 100 / denominator) >= row):
                print("  *", end = "")
            else:
                print("   ", end = "")
        print()


def drawHorizontalAxis():

    # Draw the horizontal axis
    print("+", end = "")
    for index in range(0, 11):
        print("--+", end = "")
    print("-")
    print("   ", end="")

    # Draw the horizontal dice roll numbers
    for number in range(2, 13):
        if (number < 9):
            print(number, end = "  ")
        else:
            print(number, end = " ")

def main():

    # Seed the random number generator
    random.seed(1314)

    numDiceRolls = int(input("How many times do you want to roll the dice? "))

    # Generate a dictionary of random dice roll outcomes
    dictDiceRolls = generateRolls(numDiceRolls)

    # Convert the dictionary values to a list
    listDiceRolls = generateDiceList(dictDiceRolls)

    # Output the results
    print("Results: ", listDiceRolls)
    print()

    # Draw the histogram
    drawVerticalAxis(dictDiceRolls, numDiceRolls)
    drawHorizontalAxis()

main()