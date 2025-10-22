# # iterate the every day in the index
# for cur_day in range(1, len(sentences) + 1):
#     # iterate the first till current day
#     for pre_day in range(1, cur_day + 1):
#         sentence = sentences[pre_day - 1]
#         print(f'On the {pre_day} day of Spring Festival, my parents gave me: \n{sentence}')
#     print('-'*10)#num = random.randint(1,5)
#print(f'random number: {num}')

import sys
states = {"red":4, "red_amber":3, "green":5, "amber":3}
# loop this with respect to the whole cycle time:15 secs
cycle_time = 15

#get users' steps(lasting time)
try: 
    steps = int(input("Enter a steps(integer," \
    "lasting time you want to simulate):"))
except ValueError:
      sys.exit("Please enter an integer!")

# notice if the user give the negative integer, need to show the error and cease the program
if steps < 0:
    sys.exit("Please enter a positive integer!")

# core code: determine the state at each second
t = 0   #initialize the duration/time
for t in range(steps + 1):
    left_time = t % cycle_time
    if left_time <= 3 and left_time >= 0:
        print(f"Time {t:03d} State red")
    if left_time <= 6 and left_time >= 4:
        print(f"Time {t:03d} State red_amber")
    if left_time <= 11 and left_time >= 7:
       print(f"Time {t:03d} State green")
    if left_time <= 14 and left_time >= 12:
       print(f"Time {t:03d} State amber")
    t += 1