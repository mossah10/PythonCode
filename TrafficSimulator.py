'''
Mossah Aljalal
1 MARCH 2018
Car travel time through 4 intersections, going from intersection 4 to 1.
There are four intersections in a square. Cars we are concerned with enter from
intersection 4 and exit at intersection 1. The drivers can choose to turn left
at 4, then turn right at 3, or go straight at 4, then turn left at 2, then right
at 1. Right turn is allowed, after a stop, which adds 5 seconds to time to exit
at 1. The lights at 2 and 4 have left turn arrows, and a left turn is allowed on
green, with the probability 50% of being delayed 10 seconds by oncoming traffic.
Program simulates 10,000 cars traveling through the square of four intersections
and exiting, while recording the average time to transit the square. It takes
exactly one minute to drive on one side of the square, also add the time
required to wait at each light to this travel time. Tally average time to
transit the square according to each strategy: turning left at intersection 4
every time; going straight every time; or choosing to go straight whenever
there's a green light or turning left if there's a red light or left turn arrow.
'''
import random
    
    
time = 0

def set_time_to_zero():
    global time
    time = 0

def turn_left_on_arrow():
    global time
    time +=0
    
def turn_right():
    global time
    time +=5
    
def turn_left_on_green():
    global time
    traffic = random.randint(0, 1)
    if (traffic == 0):
        time +=10
    else:
        time +=0
    
def travel_to_next_intersection():
    global time
    time +=60
    
def go_straight():
    global time
    time +=0
    
def stop_light(stop):
    global time
    time = time + stop
    
def print_time():
    print(time)  

def strategy_1():
    global time
    set_time_to_zero()
    # turn left at intersection 4
    firstLight = random.randint(1, 85)
    if (firstLight <= 10): # left arrow
        turn_left_on_arrow()   
        
    elif (firstLight > 45 ): # green light
        turn_left_on_green()
        
    else: # red light
        stop_light(35) # time spent at this red light
        
    # travel to intersection 3
    travel_to_next_intersection()
    # turn right at intersection 3
    secondLight = random.randint(1, 100)
    if (secondLight <= 30):
        turn_right()
    else: # red light
        stop_light(70) # time spent at this red light
    # travel to intersection 1
    travel_to_next_intersection()
    # go straight at intersection 1
    thirdLight = random.randint(1, 90)
    if (thirdLight <= 40): # green light
        go_straight()
    elif (thirdLight > 50):
        stop_light(50) # time spent at this red light and left arrow after it
    else:
        time +=10 # time spent waiting for left arrow to go away
    #print_time()   
    return time 
    
def strategy_2():
    global time
    set_time_to_zero()
    # go straight at intersection 4
    firstLight = random.randint(1, 85)
    if (firstLight <= 40): # green light
        go_straight() 
        
    else: # red light
        stop_light(45) # time spent at this red light and left arrow after it
        
    # travel to intersection 2
    travel_to_next_intersection()
    # turn left at intersection 2
    secondLight = random.randint(1, 95)
    if (secondLight <= 30):
        turn_left_on_green()
    elif (secondLight >80):
        turn_left_on_arrow()
    else: # red light
        stop_light(50) # time spent at this red light
    # travel to intersection 1
    travel_to_next_intersection()
    # turn right at intersection 1
    thirdLight = random.randint(1, 100)
    if (thirdLight <= 50): # green light
        turn_right()
    else:
        stop_light(50) # time spent at this red light
    #print_time()
    return time 
    
def strategy_3():
    global time
    set_time_to_zero()
    # go straight or turn left at intersection 4
    firstLight = random.randint(1, 85)
    if (firstLight <= 40): # green light, go straight
        strategy_2()   
    else:
        strategy_1()
    return time 
        
        
timeOne = 0
timeTwo = 0
timeThree = 0

for x in range(10000):
    timeOne += strategy_1()
    timeTwo += strategy_2()
    timeThree += strategy_3()
    
avgStratOne = timeOne/x
avgStratTwo = timeTwo/x
avgStratThree = timeThree/x

print("Which strategy was the best for getting through the intersections?")
print("Average time for strategy 1 was {:.2f} seconds.".format(avgStratOne))
print("Average time for strategy 2 was {:.2f} seconds.".format(avgStratTwo))
print("Average time for strategy 3 was {:.2f} seconds.".format(avgStratThree))

if (avgStratOne < avgStratTwo and avgStratOne < avgStratThree):
    print("Strategy 1 was optimal with an average time",
    "of {:.2f} seconds.".format(avgStratOne))
    
if (avgStratTwo < avgStratOne and avgStratTwo < avgStratThree):
    print("Strategy 2 was optimal with an average time",
    "of {:.2f} seconds.".format(avgStratTwo))
    
if (avgStratThree < avgStratOne and avgStratThree < avgStratTwo):
    print("Strategy 3 was optimal with an average time",
    "of {:.2f} seconds.".format(avgStratThree))
    
