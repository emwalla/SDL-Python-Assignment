
"""

Combined the last two extension prompts into one function. The max number is an argument for the program, which
asks the user for a list of factors and words to replace it.

Prints the list of chosen words and factors replaced.

"""

import argparse

def parsearguments(): # Parsing argument: argument = file name
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type = int, help = "Max number the program goes to")
    return parser.parse_args()
args = parsearguments()

length = int(input("How many factors would you like to replace with words?"))
factors = []
words = []
i = 0
while i < length:
    factor = input("Enter a factor.")
    factors.append(factor)
    word = input("Enter the word to replace that number.")
    words.append(word)
    i += 1

factors2 = list(map(int, factors)) # Converting user input to integers
nums3 = list(range(1, args.num+1))

for i in range(1, args.num + 1):
    for j in range(len(factors2)):
        if i % factors2[j] == 0: # If the number is divisble by that factor ...
            if isinstance(nums3[i-1], int): # And if the number is there ...
                nums3[i-1] = words[j] # Replace the number with the word
            else: # Or if there's already a word...
                nums3[i-1] = nums3[i-1] + words[j] # Add the other

print(nums3)
