
"""

Generates a sequence from 1 to 100, where, along with the replacements in FizzBuzz, multiples of 7 are replaced by 'Fang',
multiples of 11 are replaced by 'Bang', and numbers with multiple factors are replaced by the appropriate combination of words.

Prints the "normal" numbers and their replaced equivalent.

"""

words = ['Fizz', 'Buzz', 'Fang', 'Bang']
factors = [3, 5, 7, 11]
nums = list(range(1, 101))

for i in range(1, 101):
    for j in range(len(factors)):
        if i % factors[j] == 0: # If the number is divisble by that factor ...
            if isinstance(nums[i-1], int): # And if the number is there ...
                nums[i-1] = words[j] # Replace the number with the word
            else: # Or if there's already a word...
                nums[i-1] = nums[i-1] + words[j] # Add the other

    print(i, ':', nums[i-1])
