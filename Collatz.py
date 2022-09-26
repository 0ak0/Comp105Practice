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
steplist.insert(0, 0)
steplist.insert(1, 0)  # list position correlates to n, n starts at 2 so insert values at 0 and 1


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
            even = False
        if odd:
            m = 3 * m + 1
            step += 1
            print(step)
            odd = False

    if m == 1:
        steplist.append(step)
        n += 1
        m = n
    step = 0
    print("Added one to n, n is now " + str(n))

print("List Full!")
print("\n"
      "\n"
      "\n")  # Add new lines so that final print is distinct

#  Once the list is full, find the highest value (this will be amount of steps) and position (n)
largeststep = max(steplist)
lspos = steplist.index(largeststep)  # Find the largest value in the list, then find its position

print(str(lspos) + " has the longest Collatz Sequence at " + str(largeststep) + " steps.")
#  If this is correct, the output should be 261 steps for when n = 6171
#  This is working correctly
