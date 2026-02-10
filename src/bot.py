import random

# ---- User Inputs ----
robot_name = input("Enter robot name: ")

distance_to_target = int(input("Enter distance to target (in meters): "))

obstacle_ahead = input("Is there an obstacle ahead? (yes/no): ").lower()

# ---- Decision Making (Speed & Movement) ----
if obstacle_ahead == "yes":
    if distance_to_target > 50:
        speed = 2
        movement = "Moving slowly due to obstacle"
    else:
        speed = 1
        movement = "Crawling carefully due to nearby obstacle"
else:
    if distance_to_target > 100:
        speed = 5
        movement = "Moving fast"
    elif distance_to_target > 50:
        speed = 3
        movement = "Moving at medium speed"
    else:
        speed = 2
        movement = "Approaching target slowly"

# ---- Checkpoint Management ----
checkpoints = ["Start"]

# Simulate movement and checkpoints
distance_travelled = 0

while distance_travelled < distance_to_target:
    step = random.randint(5, 15)
    distance_travelled += step

    # Simulate unexpected direction change
    direction_change = random.choice(["Left", "Right", "Straight"])
    checkpoints.append(f"Checkpoint at {distance_travelled}m ({direction_change})")

# Optional checkpoint update
remove_choice = input("Do you want to remove the last checkpoint? (yes/no): ").lower()
if remove_choice == "yes" and len(checkpoints) > 1:
    removed = checkpoints.pop()
    print(f"Removed checkpoint: {removed}")

# ---- Trip Summary ----
print("\n----- TRIP SUMMARY -----")
print(f"Robot Name           : {robot_name}")
print(f"Total Distance       : {distance_travelled} meters")
print(f"Obstacle Ahead       : {obstacle_ahead}")
print(f"Movement Decision    : {movement}")
print(f"Speed Level          : {speed}")
print(f"Final Checkpoints    : {checkpoints}")
print("------------------------")