import random
import time
import os

WIDTH = 12
HEIGHT = 10
NUM_STEPS = WIDTH  # length of the path


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw_scene(robot, persons, walls, door):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos = [x, y]
            if pos == robot:
                print("R", end=" ")
            elif pos in persons:
                print("P", end=" ")
            elif pos in walls:
                print("W", end=" ")
            elif pos == door:
                print("D", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\nR=Robot  P=Person  W=Wall  D=Door\n")


def main():
    # Robot name
    robot_name = input("Enter Robot Name: ").strip() or "Robo"

    # Target distance
    while True:
        try:
            max_distance = int(input("Enter distance for the robot to travel: "))
            if max_distance <= 0:
                print("Distance must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    # Initialize robot
    robot = [0, random.randint(0, HEIGHT - 1)]
    door = [WIDTH - 1, random.randint(0, HEIGHT - 1)]

    speed = 1
    distance_travelled = 0
    direction = "right"
    travelling_status = "moving"
    game_over = False

    # Create obstacles
    persons = []
    walls = []
    for step in range(1, WIDTH - 1):
        y_pos_person = random.randint(0, HEIGHT - 1)
        y_pos_wall = random.randint(0, HEIGHT - 1)
        persons.append([step, y_pos_person])
        walls.append([step, y_pos_wall])

    while not game_over:
        clear()
        draw_scene(robot, persons, walls, door)

        print(f"Robot: {robot_name}")
        print(f"Distance Travelled: {distance_travelled}")
        print(f"Status: {travelling_status}")
        print(f"Current Direction: {direction}\n")

        # Stop if reached max distance
        if distance_travelled >= max_distance:
            travelling_status = "stopped"
            print("Target distance reached! GAME OVER")
            break

        robot_x, robot_y = robot
        obstacle_ahead = None
        obstacle_type = None

        # Check nearest person
        for p in persons:
            if p[1] == robot_y and p[0] > robot_x:
                if obstacle_ahead is None or p[0] < obstacle_ahead[0]:
                    obstacle_ahead = p
                    obstacle_type = "person"

        # Check nearest wall
        for w in walls:
            if w[1] == robot_y and w[0] > robot_x:
                if obstacle_ahead is None or w[0] < obstacle_ahead[0]:
                    obstacle_ahead = w
                    obstacle_type = "wall"

        # Steps to obstacle
        steps_to_obstacle = (
            obstacle_ahead[0] - robot_x if obstacle_ahead else 1
        )

        # Person logic
        if obstacle_type == "person" and steps_to_obstacle <= 1:
            print("Person ahead! Waiting 5 seconds...")
            travelling_status = "stopped"
            time.sleep(5)
            robot[0] += 1
            distance_travelled += 1
            travelling_status = "moving"
            persons.remove(obstacle_ahead)

        # Wall logic
        elif obstacle_type == "wall" and steps_to_obstacle <= 2:
            travelling_status = "stopped"
            print("Wall ahead! Choose direction: up / down / back")

            while True:
                cmd = input("Direction: ").lower()

                if cmd == "up" and robot[1] > 0:
                    robot[1] -= 1
                    direction = "up"
                    break
                elif cmd == "down" and robot[1] < HEIGHT - 1:
                    robot[1] += 1
                    direction = "down"
                    break
                elif cmd == "back" and robot[0] > 0:
                    robot[0] -= 1
                    direction = "left"
                    break
                else:
                    print("Invalid move. Try again.")

                distance_travelled += 1
                travelling_status = "moving"

        # Normal movement
        else:
            robot[0] += speed
            distance_travelled += speed
            direction = "right"
            travelling_status = "moving"

        # Boundaries
        robot[0] = min(robot[0], WIDTH - 1)
        robot[1] = max(0, min(robot[1], HEIGHT - 1))

        # Hit wall check
        if robot in walls:
            travelling_status = "stopped"
            clear()
            draw_scene(robot, persons, walls, door)
            print("Robot hit the wall! GAME OVER")
            game_over = True

        # Door check
        if robot == door:
            travelling_status = "stopped"
            clear()
            draw_scene(robot, persons, walls, door)
            print(f"{robot_name} reached the door! GAME OVER")
            game_over = True

        time.sleep(0.5)

    print(f"\nTotal Distance Travelled: {distance_travelled}")
    print(f"Final Status: {travelling_status}")
    print(f"Final Direction: {direction}")


if __name__ == "__main__":
    main()
