
"""dict={1:"Pavithra",2:"Anusha",3:"Sowmya"}
print(dict[1])

student={"name":"Pavithra",
             "age":22,
             "course":"MCA"}
print(student["name"])
student["age"]=23
student["city"]="Delhi"
print(student)
#togetvalue by uing key
print(student.get("course"))
print(student.get("country",0))
for key, value in student.items():
    print(key,value) 
    
#input dictionary from user
n=int(input("Enter number of customers: "))
user_purchases={}

for _ in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount

print("Customer Purchase Data :",user_purchases)

top_customer=max(user_purchases, key=user_purchases.get)
print(f"Top Customer: {top_customer} with purchase amount ₹ {user_purchases[top_customer]}")

low_customer=min(user_purchases, key=user_purchases.get)
print(f"Lowest Customer: {low_customer} with purchase amount ₹ {user_purchases[low_customer]}")
"""

numbers={1,2,3,4}
print(numbers)
numbers.add(5)
print(numbers)