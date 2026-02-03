# POTD 9 skel
# Author: Mackenzie Gallovitch
# Date: 2 February 2026
# Description: Dice Rolling

import sys
import random

die_sides = int(sys.argv[1])
num_die = int(sys.argv[2])

total_roll = 0

for i in range(1, num_die+1):
    roll = random.randint(1, die_sides)
    print(roll, end=" ")
    total_roll += roll
    
print("\n" + str(total_roll/num_die))
    
    

