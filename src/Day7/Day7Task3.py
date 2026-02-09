filename = input("Enter the filename to open: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet ")