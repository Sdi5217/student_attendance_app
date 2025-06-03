import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        grade TEXT,
        phone TEXT,
        email TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def add_student(name, grade, phone, email):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (name, grade, phone, email) VALUES (?, ?, ?, ?)", (name, grade, phone, email))
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def mark_attendance(student_id):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO attendance (student_id, timestamp) VALUES (?, ?)", (student_id, now))
    conn.commit()
    conn.close()

def get_attendance_stats():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''
        SELECT s.name, s.grade, COUNT(a.id) as total_attendance
        FROM students s
        LEFT JOIN attendance a ON s.id = a.student_id
        GROUP BY s.id
    ''')
    data = c.fetchall()
    conn.close()
    return data