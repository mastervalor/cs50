import csv
from cs50 import SQL

houses = []
db = SQL("sqlite:///roster.db")

# Clear tables
db.execute("DELETE FROM assignments;")
db.execute("DELETE FROM students;")
db.execute("DELETE FROM houses;")

def create_house(house, head):
    if house not in houses:
        houses.append(house)
        db.execute("INSERT INTO houses (house, head) VALUES (?, ?);", house, head)

def create_student(name):
    db.execute("INSERT INTO students (student_name) VALUES (?);", name)

def create_relation(student_id, house_id):
    db.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?);", student_id, house_id)

with open("./students.csv", "r") as csv_file:
    file = csv.DictReader(csv_file)
    for row in file:
        create_house(row["house"], row["head"])
        create_student(row['student_name'])
        student_id = db.execute("SELECT id FROM students WHERE student_name = ?;", row['student_name'])
        house_id = db.execute("SELECT id FROM houses WHERE house = ?;",  row["house"])
        create_relation(student_id[0]["id"], house_id[0]["id"])
