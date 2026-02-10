"""
Author: Edward Liao
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # Float
highest_reps = 25 # Integer
membership_active = True # Boolean

# Step c: Create a dictionary named workout_stats
# Keys are friend names (String), values are tuples of (minutes spent on three workout activities) (Integer)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (15, 30, 10),
    "Taylor": (10, 20, 15)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
workout_stats_totals = {}
for friend, activities in workout_stats.items():
    workout_stats_totals[f"{friend}_Total"] = sum(activities)
workout_stats.update(workout_stats_totals)

# Step e: Create a 2D nested list called workout_list
# Each inner list contains the workout minutes for each friend excluding totals
workout_list = []
for friend, activities in workout_stats.items():
    if not friend.endswith("_Total"):
        workout_list.append(list(activities))
# Step f: Slice the workout_list
yoga_and_running_workout_list = []
weightlifting_workout_list = []
for activities in workout_list:
    yoga_and_running_workout_list.append(activities[0:2])
    weightlifting_workout_list.append(activities[2])

print("Yoga and Running Workout List:", yoga_and_running_workout_list)
print("Weightlifting Workout List:", weightlifting_workout_list)

# Step g: Check if any friend's total >= 120
for friend, total in workout_stats_totals.items():
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name to look up their total workout minutes: ")
if friend_name in workout_stats:
    print(f"{friend_name}'s total workout minutes: {workout_stats[f'{friend_name}_Total']}")
    print(f"{friend_name}'s workout minutes for Yoga: {workout_stats[friend_name][0]}")
    print(f"{friend_name}'s workout minutes for Running: {workout_stats[friend_name][1]}")
    print(f"{friend_name}'s workout minutes for Weightlifting: {workout_stats[friend_name][2]}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
highest_total = max(workout_stats_totals.values())
lowest_total = min(workout_stats_totals.values())


highest_friends = []
lowest_friends = []
for friend, total in workout_stats_totals.items():
    if total == highest_total:
        highest_friends.append(friend)
    if total == lowest_total:
        lowest_friends.append(friend)

print(f"{highest_friends} had the highest total workout minutes of {highest_total}.")
print(f"{lowest_friends} had the lowest total workout minutes of {lowest_total}.")