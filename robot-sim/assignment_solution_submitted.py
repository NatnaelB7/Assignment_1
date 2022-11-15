from __future__ import print_function

import time
from sr.robot import *

"""
Python Script for Assignment 1

Following the definition of the functions, insert the main code. The robot's coding ought to cause it to:
	- 1) Find a silver box by looking around the domain
	- 2) Grab the closest silver box
	- 3) Move to the closest golden box
	- 4) Place a silver box next to the golden box
	- 5) Start agin from 1
The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER,
	When done, run with:
	$ python2 run.py assignment_solution_submitted.py
	
"""


a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.5
""" float: Threshold for the control of the linear distance"""

silver = True
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)                       # The Robot just waits for a second
    R.motors[0].m0.power = 0                  # The Robot will stop
    R.motors[0].m1.power = 0                  # The Robot will stop

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)                       # The Robot just waits for a second
    R.motors[0].m0.power = 0                  # The Robot will stop
    R.motors[0].m1.power = 0                  # The Robot will stop

def find_silver_token():
    """
    Function to find the closest silver token
    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

def find_golden_token():
    """
    Function to find the closest golden token
    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
    	print(dist)
    	print(rot_y)
   	return dist, rot_y
   	
tokens_collected = 0           # Initializing the number of tokens that are going to be paired together
first_iteration = True         # When silver box is closed to the golden box

while tokens_collected < 6:
    if silver == True:         # If silver is True, than we look for a silver token, otherwise for a golden one
	dist, rot_y = find_silver_token()
    else:
	dist, rot_y = find_golden_token()
    if dist==-1:               # If no token is detected, we make the robot turn 
	print("No tokens are visible to me!!")
	turn(+10, 1)
    elif dist <d_th:           # If we are close to the token, the robot will try to grab it
        print("Found it!")
        if silver == True:
		if R.grab(): 
		    print("Got it!")
		    silver = not silver  # we modify the value of the variable silver
		    if first_iteration:
		    	turn(-20, 4)
		    	first_iteration = False
		    else:
		   	turn(-20, 2)
		else:
		    print("Oh no, I'm so far away.")
		    drive(10, 0.5)
	else:                            #if gold
		if R.release():
			print("Drop it!")
			silver = not silver
			tokens_collected = tokens_collected + 1     # The collected tokens increase by one
			turn(20, 1)
			drive(10, 0.5)
		else:
		    print("Oh no, I'm so far away.")
    elif -a_th<= rot_y <= a_th:          # If the robot is well aligned with the token, we go forward
	print("Ah, that'll do.")
        drive(10, 0.5)
    elif rot_y < -a_th:  # if the robot is not well aligned with the token, we move it on the left or on the right
        print("Left a bit...")
        turn(-2, 0.5)
    elif rot_y > a_th:
        print("Right a bit...")
        turn(+2, 0.5)
