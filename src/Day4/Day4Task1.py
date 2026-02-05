contacts = {
    "Pavithra": "9876543210",
    "Ramya": "9123456780",
    "Shravya": "9001122334"
}
contacts["Diana"] = "9988776655"
contacts["Ramya"] = "9111111111"
existing_contact = contacts.get("Pavithra", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookup Results:")
print("Pavithra:", existing_contact)
print("Eve:", missing_contact)

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")