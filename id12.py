import math
"""

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""


def generate_triangle_number(n):
    return int(n*(n+1)/2)

def num_factor(n):
    count = 0
    square_root = int(math.sqrt(n)) + 1
    for x in range(1, square_root):
        if n % x == 0 and x*x != n:
            count += 2
        if n % x == 0 and x*x == n:
            count += 1

    return count

num_of_factors = 0
n = 1
while num_of_factors < 500:
    triangle_number = generate_triangle_number(n)
    num_of_factors = num_factor(triangle_number)
    n += 1

print(triangle_number)
