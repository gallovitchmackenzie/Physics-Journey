# POTD 8 skel
# Author: Mackenzie Gallovitch
# Date: 31 January 2026
# Description: POTD Calendar

import sys

month_days = int(sys.argv[1])
start_day = int(sys.argv[2])

print("su mo tu we th fr sa")

start_pad = ("   " * start_day)
print(start_pad, end="")

weekday = start_day

for day in range (1, month_days + 1):
    if day < 10:
        print(" " + str(day), end=" ")
    else:
        print(str(day), end=" ")
    weekday += 1
    if weekday == 7:
        print()
        weekday = 0