import random
import time
import os
import sys

WIDTH = 20
HEIGHT = 10
PATH_LENGTH = 80
SPEED = 0.25

PERSON_SYMBOL = "👤"
WALL_SYMBOL = "🧱"
COIN_SYMBOL = "💰"
ROBOT_SYMBOL = "🤖"
EMPTY_SYMBOL = "·"

COLOR_PERSON = "\033[33m"
COLOR_WALL = "\033[31m"
COLOR_ROBOT = "\033[36m"
COLOR_COIN = "\033[32m"
COLOR_RESET = "\033[0m"


def clear():
    sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")


def draw_scene(robot_pos, view, distance, score, direction, status):
    clear()
    print(f"Distance: {distance}  Score: {score}  Direction: {direction}  Status: {status}")
    print("-" * (WIDTH * 2))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == robot_pos:
                print(f"{COLOR_ROBOT}{ROBOT_SYMBOL}{COLOR_RESET}", end=" ")
            elif view[y][x] == "P":
                print(f"{COLOR_PERSON}{PERSON_SYMBOL}{COLOR_RESET}", end=" ")
            elif view[y][x] == "W":
                print(f"{COLOR_WALL}{WALL_SYMBOL}{COLOR_RESET}", end=" ")
            elif view[y][x] == "C":
                print(f"{COLOR_COIN}{COIN_SYMBOL}{COLOR_RESET}", end=" ")
            else:
                print(EMPTY_SYMBOL, end=" ")
        print()

    print("-" * (WIDTH * 2))


def safe_world(world, wx, wy):
    if 0 <= wy < HEIGHT and 0 <= wx < len(world[0]):
        return world[wy][wx]
    return " "


def generate_world():
    world = []
    for y in range(HEIGHT):
        row = []
        for x in range(PATH_LENGTH + WIDTH):
            row.append(random.choice([" ", " ", "P", "W", "C"]))
        world.append(row)
    return world


def get_view(world, offset):
    return [world[y][offset:offset + WIDTH] for y in range(HEIGHT)]


def main():
    robot_name = input("Enter Robot Name: ") or "Robo"

    robot_pos = [0, HEIGHT // 2]
    world = generate_world()
    offset = 0

    score = 0
    distance = 0
    direction = "right"
    status = "moving"

    while True:

        view = get_view(world, offset)
        draw_scene(robot_pos, view, distance, score, direction, status)

        x, y = robot_pos
        wx = offset + x

        front = safe_world(world, wx + 1, y)

        # PERSON
        if front == "P":
            status = "stopped"
            draw_scene(robot_pos, view, distance, score, direction, status)
            print("Person ahead! Waiting 3 seconds...")
            time.sleep(3)
            robot_pos[0] += 1

        # WALL
        elif front == "W":
            status = "stopped"
            draw_scene(robot_pos, view, distance, score, direction, status)
            print("Wall ahead! Choose direction (up/down/back/jump):")

            moved = False
            while not moved:
                cmd = input("Direction: ").lower()

                if cmd == "jump":
                    print("Jumping over wall!")
                    robot_pos[0] += 1
                    direction = "jump"
                    moved = True

                elif cmd == "up" and safe_world(world, wx, y - 1) != "W":
                    robot_pos[1] -= 1
                    direction = "up"
                    moved = True

                elif cmd == "down" and safe_world(world, wx, y + 1) != "W":
                    robot_pos[1] += 1
                    direction = "down"
                    moved = True

                elif cmd == "back" and safe_world(world, wx - 1, y) != "W":
                    robot_pos[0] -= 1
                    direction = "left"
                    moved = True

                else:
                    print("Blocked or invalid. Try again.")

        # NORMAL MOVE
        else:
            robot_pos[0] += 1
            direction = "right"

        # Clamp position
        robot_pos[0] = max(0, min(robot_pos[0], WIDTH - 1))
        robot_pos[1] = max(0, min(robot_pos[1], HEIGHT - 1))

        wx = offset + robot_pos[0]

        # Collect coin
        if safe_world(world, wx, robot_pos[1]) == "C":
            score += 20
            world[robot_pos[1]][wx] = " "

        # Collision detection
        if safe_world(world, wx, robot_pos[1]) == "W":
            status = "stopped"
            view = get_view(world, offset)
            draw_scene(robot_pos, view, distance, score, direction, status)
            print("Robot touched wall! GAME OVER")
            break

        # Scroll world
        if direction in ["right", "jump"]:
            offset += 1
            distance += 1

        status = "moving"

        if distance >= PATH_LENGTH:
            status = "stopped"
            view = get_view(world, offset)
            draw_scene(robot_pos, view, distance, score, direction, status)
            print(f"{robot_name} finished the run! GAME OVER")
            break

        time.sleep(SPEED)

    print("\n===== Final Report =====")
    print("Robot Name:", robot_name)
    print("Distance:", distance)
    print("Score:", score)
    print("Last Direction:", direction)
    print("Final Status:", status)


if __name__ == "__main__":
    main()
