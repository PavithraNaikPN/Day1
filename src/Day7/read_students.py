import csv

with open("D:\DS_AL_Internship\src\Day7\students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
