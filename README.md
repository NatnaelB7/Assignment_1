Assignment 1 - Python Robotics Simulator
==========================================
This is a simple robot simulator coded by Natnael Berhanu Takele that pairs the silver and golden boxes.

Installing and Running
------------------------
The simulator requires a Python 2.7 installation, the pygame library, PyPyBox2D, and PyYAML.
When done, you can run the program with:
>$ python run.py assignment_solution_submitted.py

Robot 
------------
### Motors
The simulated robot has two motors configured for skid steering, connected to a two-output Motor Board. The left motor is connected to output **0** and the right motor to output **1**.

## Pseudocodes
>The pseudocodes are provided over here for an overview of the program.



       While the collected token is less than 6:
           if silver is true:
               find a silver token
           else:
               find a golden token
           if no token is detected:
               turn 
           else if the linear distance < threshold:
               simply display its current status
               if silver is true:
                      if the robot is ready to grab the token:
                          simply display its current status
                          silver = not silver
                          if the first iteration of pair works:
                              turn
                          else:
                              turn
                      else:
                          move forward 
               else:
                      if the robot is ready to release the token:
                          simply display its current status
                          silver = not silver
                          The collected tokens increase by one
                          turn and move forward

                      else:
                          simply display its current status 
           else if the robot is well aligned:
                move forward
           else if the robot is on the left:
                turn to the right
           else
                turn to the left
    
               
          
