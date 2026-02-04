
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
    
Purchase={
    "name":"Laptop",
    "amount":75000,
    }
for name,amount in Purchase.items():
        print(f"{name} spent ₹{amount}")
        print("Total:",Purchase.values())
        n=int(input("Enter the number of custmer:"))
        user_Purchase={}
for i in range(n):
    name=input("Enter the name:")
    amount=int(input(f"Enter the amount for {name}:"))
    user_Purchase[name]=amount
print("Customer Purchases Data:",user_Purchase)
top_customer=max(user_Purchase,key=user_Purchase.get)
print("Top Spending Customer:",top_customer)
Last_customer=min(user_Purchase,key=user_Purchase.get)
print("Top Spending Customer:",Last_customer)
"""

numbers={1,2,3,4}
print(numbers)
numbers.add(5)
print(numbers)