# Task 4 - Triathlon Prizes
# Design a programme that determines the prizes given to participants in a triathlon 
# based on their total times. Your programme should take in and display the individual times 
# in minutes for all three events then add them all up for an overall score.
# Prizes are then awarded according to the following schema:
# For an overall time of 0-100 minutes - the award is the Provincial Colours;
# For an overall time of 101-105 minutes - the award is the Provincial Half Colours;
# For an overall time of 106-110 minutes - the award is the Provincial Scroll;
# For an overall time of 111+ minutes - there is no award.

# Part 1 : Get the athlete to enter their trial times by section (swim, cycle, run):
swim = int(input("Please enter your time in minutes for the 1 Km swim : "))
cycle = int(input("Please enter your time in minutes for the 10 Km cycle : "))
run = int(input("Please enter your time in minutes for the 10 Km run : "))
total_time = swim + cycle + run  #in minutes

# Changing total_time variable into hours and minutes as per Issue-1
hours = total_time//60
minutes = total_time % 60
print()
print("Thank you! Your total time was ", hours, "hour(s) and", minutes, "minutes. ")

# Part 2 - Now let's work out what prize the athlete gets :
if total_time < 100 :
    greeting = "Congratulations! This means you have been awarded the provincial colours."

elif total_time >= 101 and total_time <= 105:
    greeting = "Congratulations! You have been awarded the provincial half colours."

elif total_time >= 106 and total_time <= 110:
    greeting = "Congratulations! You have been awarded the provincial scroll."

elif total_time >= 111:
    greeting = "There is no award for that time but well done for finishing!"

else:
    greeting = "Thanks for taking part in the event! Hope you had fun!"

print(greeting)
