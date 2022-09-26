# Name Reverser
# Program should read single word input from user (until "quit" is given)
# Program should then output each string from user, in order not including "quit"
# Each string output should be reversed (eg: Apple -> elppA)

# Variables created
n = 0
quitnum = 0
loop = True
inputlist = []
outputlist = []

# Gather input from user, add this input to a list, wait for "quit"
while loop:
    inputlist.append(input('Type a name ("quit" to stop): '))
    if inputlist[n] == "quit":
        loop = False
        quitnum = n
    n += 1

# Reverse each string inside the list, add to new list
n = 0
while n < quitnum:
    outputlist.append(inputlist[n][::-1])
    n += 1

# Add each item from new list to string and print
outputstring = ""
n = 0
for x in outputlist:
    outputstring = outputstring + " " + outputlist[n]
    n += 1
print(outputstring)
