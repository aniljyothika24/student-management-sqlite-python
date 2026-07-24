import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id TEXT PRIMARY KEY,
    name TEXT,
    gender TEXT,
    course TEXT,
    marks INTEGER
) """)
conn.commit()


def add_student():
    add_id = input("Enter the id number of the student: ")
    add_name = input("Enter the name of the student: ")
    add_gender = input("Enter the gender of the student: ")
    add_course = input("Enter the course of the student: ")
    add_marks = input("Enter the marks of the student: ")
    cursor.execute("INSERT INTO students VALUES(?,?,?,?,?)",(add_id,add_name,add_gender,add_course,add_marks))
    conn.commit()
    print("\n Details added successfully")

def display_students():
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

def update_student():
    update_id = input("Enter the id number of the student whole details to be updated: ")
    update_field = int(input("Select the field to be updated: \n1.id \n2.name \n3.gender \n4.course \n5.marks \nSelect(1/2/3/4/5): "))
    new_value = input("Enter the new value to be updated: ")
    if update_field == 1:
        cursor.execute("UPDATE students SET id = ? WHERE id = ? ",(new_value, update_id))
        conn.commit()
    elif update_field == 2:
        cursor.execute("UPDATE students SET name = ? WHERE id = ? ",(new_value, update_id))
        conn.commit()
    elif update_field == 3:
        cursor.execute("UPDATE students SET gender = ? WHERE id = ? ",(new_value, update_id))
        conn.commit()
    elif update_field == 4:
        cursor.execute("UPDATE students SET course = ? WHERE id = ? ",(new_value, update_id))
        conn.commit()
    elif update_field == 5:
        cursor.execute("UPDATE students SET marks = ? WHERE id = ? ",(new_value, update_id))
        conn.commit()
    else:
        print("Inavlid choice")

def delete_student():
    delete_id = input("Enter the id number of the student whose details to be deleted: ")
    cursor.execute("DELETE FROM students WHERE id = ?",(delete_id))

def search_student():
    search_id = input("Enter the id number of the student to be searched: ")
    cursor.execute("SELECT * FROM students WHERE id = ?",(search_id))
    row = cursor.fetchone()
    print(row)


while True:
    choice = int(input("\n 1.Add Student \n2.Display Students \n3.Update Students \n4.Delete Student \n5.Search Student \n6.Exit \n"))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice == 6:
        exit()
    else:
        print("Invalid Choice")

conn.close()