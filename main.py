import sqlite3
import random

school = sqlite3.connect('mydatabase.db')
sql = school.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students'
            '(student_ID INTEGER, student_name TEXT, age INTEGER, grade TEXT);')

# sql.execute(f'INSERT INTO students(student_ID, student_name, age, grade) VALUES (0, "Kay", 18, "A");')
# sql.execute(f'INSERT INTO students(student_ID ,student_name, age, grade) VALUES (1, "Lisa", 16, "C");')
# sql.execute(f'INSERT INTO students(student_ID ,student_name, age, grade) VALUES (2, "Dan", 15, "D");')
# sql.execute(f'INSERT INTO students(student_ID ,student_name, age, grade) VALUES (3, "Lord", 14, "F");')
# sql.execute(f'INSERT INTO students(student_ID ,student_name, age, grade) VALUES (4, "Salamon", 19, "A");')
# sql.execute(f'INSERT INTO students(student_ID ,student_name, age, grade) VALUES (5, "Penny", 17, "B");')

school.commit()

def get_student_by_name(name):
    sql.execute('SELECT * FROM students WHERE student_name = ?', (name, )).fetchall()
    result = sql.fetchall()
    if result:
        print(result)
    else:
        print(f"No student found with the name '{name}'")


def update_student_grade(grade, name):
    sql.execute('UPDATE students SET grade = ? WHERE student_name = ?', (grade, name))
    school.commit()

def delete_student(name):
    sql.execute('DELETE FROM students WHERE student_name = ?', (name, ))
    school.commit()


while True:
    action = input('Enter the command: ')
    if action.lower() == 'search':
        names = input('Enter student name: ')
        get_student_by_name(names.title())
    elif action.lower() == 'update':
        names = input('Enter student name: ')
        grade = input('Enter garde: ')
        update_student_grade(grade, names.title())
    elif action.lower() == 'delete':
        names = input('Enter student name: ')
        delete_student(names.title())
    else:
        print('WTF?!')