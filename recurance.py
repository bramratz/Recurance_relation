#! usr/bin/env python

"""
Given two positive integers, n and m, returns the total number of
rabbit pairs that will be present after n months. Assumes starting with
1 pair. Every rabit takes a month to mature. Each pair can produce offstring,
one male and one female baby rabbit (ie. a pair), each month once maturaity is 
reached. Rabbits live for m months before they die.
"""

n = 6 # Total number of months 
m = 3 # Months before death

def mortalRabbits (nMonths: int, mLive: int) -> int:
    """
    Given the number the total number of months the simulation should be 
    run and the number of months each rabbit has left to live, returns 
    an integer with the number of living rabbits after nMonths.
    """
    # Create list of length mLive to keep track of how many living rabbits 
    #   are still in the simulation
    alive = [0] * mLive
    
    # Always start with one rabbit 
    alive[-1] = 1
    
    # Iterate over n months starting from month 2
    for i in range(1, nMonths):
        # New babies born are equal to the number of adults present in 
        #   the population. Sum excluding the furthest column in the array
        #   as these will be babies in the first month and are unable 
        #   to reproduce 
        newBabies = sum(alive[:-1])
      
        # Shift adults left 1 position (getting older)
        alive[:-1] = alive[1:]
        
        # Add new babies to the list 
        alive[-1] = newBabies
    
    # After n months the total number of rabbits will be the total number 
    # of individuals (both babies and adults) present in the array
    return sum(alive)

# Calculate total num pairs in final round  
living = mortalRabbits(n, m)
print(f"The total number of pairs is: {living}")