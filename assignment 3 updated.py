from turtle import *
# speed(0)  # Uncomment this to speed up the turtle drawing

### Task 1: Fractals
### Task 1A: Peano Curve
def peano(level, length):
    # sequence of turns: r > l > l > l > r > r > r > l
    if level == 0:
        #every single line will turn 45 degree first in this code (starting orientation)
        rt(45)
        distance = length
        fd(distance)
    else:
        #distance of each length from top left to bottom right divide by 3
        distance = length / 3
        peano(level - 1, distance) 
        #right turns turn additional 45 to make 90 for every line
        rt(45)
        peano(level - 1, distance)
        #left turns turn additional 135 degrees to compensate for the rt 45 earlier
        lt(135)
        peano(level - 1, distance) 
        lt(135)
        peano(level - 1, distance)
        lt(135)
        peano(level - 1, distance) 
        rt(45)
        peano(level - 1, distance)
        rt(45)
        peano(level - 1, distance) 
        rt(45)
        peano(level - 1, distance)
        lt(135)
        peano(level - 1, distance)






### Test Cases: uncomment the lines below to check
# peano(1, 400)
# peano(2, 400)
# peano(0, 400)



### Task 1B: Sierpinski Triangle
def sierpinski(level, length):
    if level == 1:
        distance = length
        fd(distance)
        lt(120)
        fd(distance)
        lt(120)
        fd(distance)
        lt(120)
    else:
        distance = length / 2
        sierpinski(level - 1, distance)
        lt(60)
        fd(distance)
        rt(60)
        sierpinski(level - 1, distance)
        rt(60)
        fd(distance)
        lt(60)
        sierpinski(level - 1, distance)
        bk(distance)

### Test Cases: uncomment the lines below to check
# sierpinski(1, 400)
# sierpinski(2, 400)
# sierpinski(3, 400)



### Task 1C: Arrowhead Sierpinski
def upside_arrowhead(level, length):
    #sequence: l > r > r > l
    if level == 1:
        distance = length/2
        lt(60)
        fd(distance)
        rt(60)
        fd(distance)
        rt(60)
        fd(distance)
        lt(60)

    else:
        distance = length/2
        lt(60)
        reverse_arrowhead(level - 1, distance)
        rt(60)
        upside_arrowhead(level - 1, distance)
        rt(60)
        reverse_arrowhead(level - 1, distance)
        lt(60)

def reverse_arrowhead(level, length):
    if level == 1:
        distance = length /2
        rt(60)
        fd(distance)
        lt(60)
        fd(distance)
        lt(60)
        fd(distance)
        rt(60)

    else:
        distance = length / 2
        rt(60)
        upside_arrowhead(level - 1, distance)
        lt(60)
        reverse_arrowhead(level - 1, distance)
        lt(60)
        upside_arrowhead(level - 1, distance)
        rt(60)



### Test Cases: uncomment the lines below to check
# upside_arrowhead(4, 200)
# reverse_arrowhead(4, 200)



### Task 2: Golden Ratio
### Task 2A: Recursive Golden Ratio
def recursive_phi(n):
    if n == 0:
        return 1
    else:
        return (1/recursive_phi(n-1)) + recursive_phi(0)


### Test Cases: uncomment the lines below to check
# print(recursive_phi(0))
# print(recursive_phi(25))



### Task 2B: Iterative Golden Ratio
def iterative_phi(n):
    approxVal = 1
    for i in range(n):
        approxVal = 1 + 1/approxVal
    return approxVal


# print(iterative_phi(5))
# print(iterative_phi(25))



### Task 3: Randomness
### Task 3A: Check Outside
from math import *

def distance(x1, y1, x2, y2):
    dx, dy = x1-x2, y1-y2
    return sqrt(dx*dx + dy*dy)

def check_outside(size, x_coord, y_coord):
  dist = distance(0,0,x_coord,y_coord)
  return dist > (size + 1)


### Test Cases: uncomment the lines below to check
# print(check_outside(0.4, 1, 1))
# print(check_outside(0.5, 1, 1))



### Task 3B: Check String
def check_string(coord, size, x_coord, y_coord):

    return (coord > x_coord + size or coord < x_coord - size) and \
        (coord > y_coord + size or coord < y_coord - size)

### Test Cases: uncomment the lines below to check
# print(check_string(0, 0.005, 0.1, 0.1))
# print(check_string(0, 0.1, 0.1, 0.1))



### Task 3C: Mosquito Carlo
from random import uniform
def monte_carlo_mosquito(string_dist, size):
    timesHit = 0
    total = 0

    for i in range(100000):

        total += 1
        x,y = uniform(-1,1),uniform(-1,1)

        #if its outside completely = miss
        if check_outside(size,x,y):
            timesHit+=0
        else:
            #idea: creates a list that appends True/False depending on what check_string() outputs
            newList = []
            #for loop that checks for every string if check_string returns a True 
            totString = 0
            while totString <= 1:
                check = check_string(totString,size,x,y) and check_string(-totString,size,x,y)
                newList.append(check)
                totString += string_dist
            timesHit += False in newList

    return timesHit/total

  
### Test Cases: uncomment the lines below to check
print(monte_carlo_mosquito(0.2, 0.05))
print(monte_carlo_mosquito(0.2, 0.5))