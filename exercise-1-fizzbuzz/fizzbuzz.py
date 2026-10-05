
"""    

Generates a sequence from 1 to 100, where multiples of 3 are replaced by 'Fizz', multiples of 5
are replaced by 'Buzz', and multiples of both 3 and 5 are replaced by 'FizzBuzz'.

Prints the "normal" numbers and their FizzBuzz equivalent. 

"""

fizzbuzzlist = []
for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzzlist.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzzlist.append("Fizz")
    elif i % 5 == 0:
        fizzbuzzlist.append("Buzz")
    else:
        fizzbuzzlist.append(i)

    print(i, ':', fizzbuzzlist[i-1])
