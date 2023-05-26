import sqlite3

conn = sqlite3.connect('teachers.db')
cur = conn.cursor()

def get_student_info(student_id):
    cur.execute(f"SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name FROM Students JOIN School ON Students.School_Id=School.School_Id WHERE Students.Student_Id={student_id};")
    row = cur.fetchone()
    if row:
        student_id = row[0]
        student_name = row[1]
        school_id = row[2]
        school_name = row[3]
        print(f"ID Студента: {student_id}\nИмя студента: {student_name}\nID школы: {school_id}\nНазвание школы: {school_name}")
    else:
        print("Студент не найден")
get_student_info(201)
conn.close()