"""file=open("sample.txt","w")
file.write("hello,This is a  file handling example.")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

with open("sample.txt","r") as file:
    content=file.read()
    print(content)
    
try:
    with open("missing.txt","r") as file:
       print(file.read())
       
except FileNotFoundError:
    print("The file 'missing.txt' does not exist.")
  
import csv
with open("D:\DS_AL_Internship\src\Day7\data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
   """
import pandas as pd
file_path = "D:\DS_AL_Internship\src\Day7\data.xlsx"

df = pd.read_excel(file_path)
print(df)



