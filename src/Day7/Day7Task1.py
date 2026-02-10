name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a", encoding="utf-8") as file:
    file.write(f"Name: {name}, Daily Goal: {goal}\n")

print("Journal updated successfully!")