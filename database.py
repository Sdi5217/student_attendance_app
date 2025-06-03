import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            grade TEXT,
            phone TEXT,
            email TEXT,
            birthday TEXT,
            address TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, grade, phone, email, birthday, address):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO students (name, grade, phone, email, birthday, address)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, grade, phone, email, birthday, address))
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT id, name, grade, phone, email, birthday, address FROM students')
    students = c.fetchall()
    conn.close()
    return students

def search_students_by_grade(grade):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT id, name, grade, phone, email, birthday, address FROM students WHERE grade = ?', (grade,))
    students = c.fetchall()
    conn.close()
    return students

def mark_attendance(student_id):
    from datetime import datetime
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    c.execute('INSERT INTO attendance (student_id, date) VALUES (?, ?)', (student_id, today))
    conn.commit()
    conn.close()

def get_attendance_stats():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        SELECT s.name, s.grade, COUNT(a.id) as total_attendance
        FROM students s
        LEFT JOIN attendance a ON s.id = a.student_id
        GROUP BY s.id
    ''')
    stats = c.fetchall()
    conn.close()
    return stats
