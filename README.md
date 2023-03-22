# Word-Change-Solver
Solves the word change puzzles.

# How to Solve the Puzzles?
To solve every answer you need to change one letter from the last answer from the last puzzle.

# Example
## Puzzle
Outer garment:    coat

Water vessel:     boat

Wild pig:         boar

Sound of a lion:  roar

Traveled on: ____

# How the Solver Works
It does a brute force to find all of the possible solutions. It does this by going through each character in the word entered and loops through each letter of the English alphabet. When looping through the program checks if it is a word or not. If it is a word it will be added into a list to be shown at the end of the program.

# Use of Program Using the Example Above
INPUT:

Enter the last word in the puzzle: roar

OUTPUT:

Testing: ['a', 'o', 'a', 'r'] (False)

Testing: ['b', 'o', 'a', 'r'] (True)

Testing: ['c', 'o', 'a', 'r'] (False)

Testing: ['d', 'o', 'a', 'r'] (False)

Testing: ['e', 'o', 'a', 'r'] (False)

Testing: ['f', 'o', 'a', 'r'] (False)

Testing: ['g', 'o', 'a', 'r'] (False)

Testing: ['h', 'o', 'a', 'r'] (True)

Testing: ['i', 'o', 'a', 'r'] (False)

Testing: ['j', 'o', 'a', 'r'] (False)

Testing: ['k', 'o', 'a', 'r'] (False)

Testing: ['l', 'o', 'a', 'r'] (False)

Testing: ['m', 'o', 'a', 'r'] (False)

Testing: ['n', 'o', 'a', 'r'] (False)

Testing: ['o', 'o', 'a', 'r'] (False)

Testing: ['p', 'o', 'a', 'r'] (False)

Testing: ['q', 'o', 'a', 'r'] (False)

Testing: ['r', 'o', 'a', 'r'] (True)

Testing: ['s', 'o', 'a', 'r'] (True)

Testing: ['t', 'o', 'a', 'r'] (False)

Testing: ['u', 'o', 'a', 'r'] (False)

Testing: ['v', 'o', 'a', 'r'] (False)

Testing: ['w', 'o', 'a', 'r'] (False)

Testing: ['x', 'o', 'a', 'r'] (False)

Testing: ['y', 'o', 'a', 'r'] (False)

Testing: ['z', 'o', 'a', 'r'] (False)

Testing: ['r', 'a', 'a', 'r'] (False)

Testing: ['r', 'b', 'a', 'r'] (False)

Testing: ['r', 'c', 'a', 'r'] (False)

Testing: ['r', 'd', 'a', 'r'] (False)

Testing: ['r', 'e', 'a', 'r'] (True)

Testing: ['r', 'f', 'a', 'r'] (False)

Testing: ['r', 'g', 'a', 'r'] (False)

Testing: ['r', 'h', 'a', 'r'] (False)

Testing: ['r', 'i', 'a', 'r'] (False)

Testing: ['r', 'j', 'a', 'r'] (False)

Testing: ['r', 'k', 'a', 'r'] (False)

Testing: ['r', 'l', 'a', 'r'] (False)

Testing: ['r', 'm', 'a', 'r'] (False)

Testing: ['r', 'n', 'a', 'r'] (False)

Testing: ['r', 'o', 'a', 'r'] (True)

Testing: ['r', 'p', 'a', 'r'] (False)

Testing: ['r', 'q', 'a', 'r'] (False)

Testing: ['r', 'r', 'a', 'r'] (False)

Testing: ['r', 's', 'a', 'r'] (False)

Testing: ['r', 't', 'a', 'r'] (False)

Testing: ['r', 'u', 'a', 'r'] (False)

Testing: ['r', 'v', 'a', 'r'] (False)

Testing: ['r', 'w', 'a', 'r'] (False)

Testing: ['r', 'x', 'a', 'r'] (False)

Testing: ['r', 'y', 'a', 'r'] (False)

Testing: ['r', 'z', 'a', 'r'] (False)

Testing: ['r', 'o', 'a', 'r'] (True)

Testing: ['r', 'o', 'b', 'r'] (False)

Testing: ['r', 'o', 'c', 'r'] (False)

Testing: ['r', 'o', 'd', 'r'] (False)

Testing: ['r', 'o', 'e', 'r'] (False)

Testing: ['r', 'o', 'f', 'r'] (False)

Testing: ['r', 'o', 'g', 'r'] (False)

Testing: ['r', 'o', 'h', 'r'] (False)

Testing: ['r', 'o', 'i', 'r'] (False)

Testing: ['r', 'o', 'j', 'r'] (False)

Testing: ['r', 'o', 'k', 'r'] (False)

Testing: ['r', 'o', 'l', 'r'] (False)

Testing: ['r', 'o', 'm', 'r'] (False)

Testing: ['r', 'o', 'n', 'r'] (False)

Testing: ['r', 'o', 'o', 'r'] (False)

Testing: ['r', 'o', 'p', 'r'] (False)

Testing: ['r', 'o', 'q', 'r'] (False)

Testing: ['r', 'o', 'r', 'r'] (False)

Testing: ['r', 'o', 's', 'r'] (False)

Testing: ['r', 'o', 't', 'r'] (False)

Testing: ['r', 'o', 'u', 'r'] (False)

Testing: ['r', 'o', 'v', 'r'] (False)

Testing: ['r', 'o', 'w', 'r'] (False)

Testing: ['r', 'o', 'x', 'r'] (False)

Testing: ['r', 'o', 'y', 'r'] (False)

Testing: ['r', 'o', 'z', 'r'] (False)

Testing: ['r', 'o', 'a', 'a'] (False)

Testing: ['r', 'o', 'a', 'b'] (False)

Testing: ['r', 'o', 'a', 'c'] (False)

Testing: ['r', 'o', 'a', 'd'] (True)

Testing: ['r', 'o', 'a', 'e'] (False)

Testing: ['r', 'o', 'a', 'f'] (False)

Testing: ['r', 'o', 'a', 'g'] (False)

Testing: ['r', 'o', 'a', 'h'] (False)

Testing: ['r', 'o', 'a', 'i'] (False)

Testing: ['r', 'o', 'a', 'j'] (False)

Testing: ['r', 'o', 'a', 'k'] (False)

Testing: ['r', 'o', 'a', 'l'] (False)

Testing: ['r', 'o', 'a', 'm'] (True)

Testing: ['r', 'o', 'a', 'n'] (True)

Testing: ['r', 'o', 'a', 'o'] (False)

Testing: ['r', 'o', 'a', 'p'] (False)

Testing: ['r', 'o', 'a', 'q'] (False)

Testing: ['r', 'o', 'a', 'r'] (True)

Testing: ['r', 'o', 'a', 's'] (False)

Testing: ['r', 'o', 'a', 't'] (False)

Testing: ['r', 'o', 'a', 'u'] (False)

Testing: ['r', 'o', 'a', 'v'] (False)

Testing: ['r', 'o', 'a', 'w'] (False)

Testing: ['r', 'o', 'a', 'x'] (False)

Testing: ['r', 'o', 'a', 'y'] (False)

Testing: ['r', 'o', 'a', 'z'] (False)

Potential solutions:

boar

hoar

soar

rear

road

roam

roan
