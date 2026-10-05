import random
import numpy as np

def powertracker():

    """

    Generates a random integer between 1 and 20, randomly chooses to cube or square the number, tracks
    the largest and smallest results, then checks if the current result is divisible by the previous.

    Program exits when the current result is divisible by the previous (and the previous is not one), 
    then prints the largest and smallest results, the result that caused the loop to break, 
    and the total number of iterations.

    """

    results = []
    numiter = 1 # Starting the loop number as 1, so first loop = loop # 1

    while True: # Loop runs continuously UNTIL the break condition is met
        randnum = random.randint(1, 20)
        randchoose = random.randint(1, 2) # Choose to square or cube the number

        if randchoose == 1: # Number is going to be squared
            randnum = randnum ** 2
            results.append(randnum)
            print(f'Loop {numiter}: {np.sqrt(randnum):.0f}^2 = {randnum}')
        elif randchoose == 2: # Number is going to be cubed
            randnum = randnum ** 3
            results.append(randnum)
            print(f'Loop {numiter}: {np.cbrt(randnum):.0f}^3 = {randnum}')

        smallest = min(results)
        largest = max(results)

        numiter += 1

        # Can start to evaluate conditions for breaking after at least 2 nums in results list (numiter > 2)
        if numiter > 2 and results[-2] != 1: # Ensures previous result is not 1
            if results[-1] % results[-2] == 0:
                break

    # Final print statements
    print(f'The smallest result is {smallest}.')
    print(f'The largest result is {largest}.')
    print(f'The loop was broken when {results[-1]} was divisible by {results[-2]}.')
    print(f'The number of loops was {numiter-1}.')

powertracker()
