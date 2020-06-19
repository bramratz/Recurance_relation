#! usr/bin/env python

"""
Given two positive integers, n and m, returns the total number of
rabbit pairs that will be present after n months. Assumes starting with
1 pair. Every rabit takes a month to mature. Each pair can produce offstring,
one male and one female baby rabbit (ie. a pair), each month once maturaity is 
reached. Rabbits live for m months before they die.
"""
from collections import defaultdict

n = 6 # Total number of months 
m = 3 # Months before death

alive = defaultdict(int) # initialize default dictionary


def newNumAdults(adultsPrevRound: int, babiesPrevRound: int) -> int:
    """Calculates the number of adults in the current round"""
    return (adultsPrevRound + babiesPrevRound)

# Starting values 
Adults = 0 
Babies = 0

# Skips month 1 since the change from month 1 - 2 is 0 as the 1 baby pair
# in the first month simply matures to an adult by month 2, no reproduction
# takes place between 1 and 2 months 
for i in range(n-1):
    if i == 0:
        Adults += 1
    else:
        newAdults = newNumAdults(Adults, Babies) # New num of adults 
        newBabies = Adults
        
        # Update counts
        Adults = newAdults
        Babies = newBabies
        
# Calculate total num pairs in final round  
totalPairs = Adults + Babies
print(f"The total number of pairs is: {totalPairs}")

