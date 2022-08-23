# we just what to get all email addresses from database
contacts = {
    "number of students": 4,
    "data":
        [
            {"name": "Sarah Holdrness", "email": "sarag@example.com"},
            {"name": "Harry Potter", "email": "harry@example.com"},
            {"name": "Hermione Granger", "email": "hermione@example.com"},
            {"name": "Ron Wesley", "email": "ron@example.com"}
        ]
}
print(contacts["number of students"])
for student in contacts["data"]:
    print(student["email"])
