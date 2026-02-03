total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
share = total_bill / people
print(f"Total Bill: {total_bill}. Each person pays: {share}")
print(type(total_bill))
print(type(people))
print(type(share))