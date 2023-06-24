# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать 
# информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3
def get_student(student_id):
    connection = sqlite3.connect("teachers.db")
    cursor = connection.cursor()
    query = """SELECT * FROM School JOIN Students ON School.School_id = Students.School_id WHERE Students.Student_id = ?"""
    cursor.execute(query, (student_id,))
    record = cursor.fetchall()
    #print(record)
    for i in record:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
        print('ID Студента: ', i[3])
        print('Имя студента: ', i[4])
        print('ID школы: ', i[0])
        print('Название школы: ', i[1])

get_student(203)

