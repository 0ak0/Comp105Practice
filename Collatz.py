# The Collatz Problem
# n can be any number
# if n is even: n = n/2
# if n is odd: n = 3n+1
# Theoretically, every number should end at 1
# Find the largest starting number (n) under 10,000 that has the longest sequence

# Starting variable
n = 2  # n cannot start at 0 or 1
even = False
odd = False
step = 0
steplist = []

# Function to check for evens or odds
def evencheck(num):
    global even
    global odd
    if num % 2 == 0:  # Use a modulus to check for remainder when dividing by 2. Evens should have no remainder
        even = True
        print("Logged an Even")
    else:
        odd = True
        print("Logged an Odd")

# Begin sequence and count each step
# Loop here is used until n (the start) hits 10,000
# Log step count in list, with n (starting number) as position in list

m = n

while n < 10000:
    while m != 1:
        evencheck(m)
        if even:
            m = m / 2
            step += 1
            print(step)
        if odd:
            m = 3 * m + 1
            step += 1
            print(step)

    if m == 1:
        steplist.append(step)
        step = 0
    n += 1
    print("Added one to n, n is now " + str(n))

print(steplist)
