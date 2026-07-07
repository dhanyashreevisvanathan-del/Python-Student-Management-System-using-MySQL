import mysql.connector as sql

mycon = sql.connect(
    host="localhost",
    user="root",
    password="....",
    database="classroom"
)

mycur = mycon.cursor()

query = """
CREATE TABLE IF NOT EXISTS students(
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    age INT NOT NULL,
    course VARCHAR(20)
)
"""
mycur.execute(query)


def add_student():
    stud_id = int(input("Enter the student ID: "))
    name = input("Enter the student name: ")
    age = int(input("Enter the age: "))
    course = input("Enter the course: ")

    query = "INSERT INTO students VALUES (%s, %s, %s, %s)"
    mycur.execute(query, (stud_id, name, age, course))
    mycon.commit()
    print("Student added successfully.")


def view_student():
    query = "SELECT * FROM students"
    mycur.execute(query)
    datas = mycur.fetchall()

    for data in datas:
        print(data)


def search_student():
    sid = int(input("Enter the student ID: "))

    query = "SELECT * FROM students WHERE student_id = %s"
    mycur.execute(query, (sid,))

    data = mycur.fetchone()

    if data:
        print(data)
    else:
        print("Student not found.")


def update_student():
    sid = int(input("Enter the student ID that you want to update: "))

    print("1. Name")
    print("2. Age")
    print("3. Course")

    ch = int(input("Enter your choice: "))
    new_data = input("Enter the new data: ")

    if ch == 1:
        query = "UPDATE students SET name = %s WHERE student_id = %s"
        mycur.execute(query, (new_data, sid))

    elif ch == 2:
        query = "UPDATE students SET age = %s WHERE student_id = %s"
        mycur.execute(query, (new_data, sid))

    elif ch == 3:
        query = "UPDATE students SET course = %s WHERE student_id = %s"
        mycur.execute(query, (new_data, sid))

    else:
        print("Invalid choice.")
        return

    if mycur.rowcount > 0:
        mycon.commit()
        print("Student updated successfully.")
    else:
        print("Student ID not found.")


def delete_student():
    sid = int(input("Enter the ID that you want to delete: "))

    query = "DELETE FROM students WHERE student_id = %s"
    mycur.execute(query, (sid,))

    if mycur.rowcount > 0:
        mycon.commit()
        print("Student deleted successfully.")
    else:
        print("Student ID not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_student()

    elif ch == 3:
        search_student()

    elif ch == 4:
        update_student()

    elif ch == 5:
        delete_student()

    elif ch == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

mycur.close()
mycon.close()