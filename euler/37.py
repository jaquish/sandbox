from __future__ import division
import random

# running list of number of plates found before first 'win'
attempts = []
run_sum = 0
run_attempts = 0

# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# reset every road trip
found = set([])

# loop forever
while (1):

    while(1):
        plate = random.randrange(1000) # 000 to 999
        if ( (1000 - plate) in found):
            break
        else:
            found.add(plate)
    
    plate_count = len(found) + 1

    # cleanup
    found = set()

    attempts.append( plate_count )

    run_sum += plate_count
    run_attempts += 1
    # print run_attempts

    if (run_attempts % 1000 == 0):
        print "trips = ", run_attempts, "running avg = ", run_sum / run_attempts