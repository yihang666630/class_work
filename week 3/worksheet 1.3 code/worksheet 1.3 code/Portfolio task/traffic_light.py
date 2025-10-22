"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""
# Your name: Yihang Yu
# Your student ID: 201913006
# You state that the code submitted is wholly written by yourself. 
# Date: 25/9/2025

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
"""
red: 0,1,2,3; red_amber: 4,5,6; green: 7,8,9,10,11; 
amber: 12,13,14; cycle_time = 15; entire index: 4 Notice: change the state display when the t > = duration
"""

maxtime = int(input("Enter the steps (in seconds): "))  # read an integer number of steps (>0)
#when the input steps is less than the cycle time
tup_states = tuple(states.items())

#initialize the state and duration
current_state_idx = 0
duration_in_cur_stat = 0
for systime in range(maxtime + 1):    #the whole stpes/time range
    state, duration = tup_states[current_state_idx]
    print(f"Time {systime:03} State {state}")  #print before updating the state
#(consider the initial state at time 0)

# update the duration in current state
    duration_in_cur_stat += 1

# core: update the index to display the right/next state
    if duration_in_cur_stat == duration:
       current_state_idx = (current_state_idx + 1) % len(tup_states)
       duration_in_cur_stat = 0 
       #reset the duration for the new state(avoid the wrong state display)


# Simulate the traffic light system up to time=maxtime in 1-second steps
# At the end of each step you should output the time and state using the statement on line 14