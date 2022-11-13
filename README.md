# The Pseudocode for the Assignment 1


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
    
               
          
