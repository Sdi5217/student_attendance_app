import streamlit as st
import pandas as pd
from database import init_db, add_student, get_students, mark_attendance, get_attendance_stats
from export import export_excel, export_pdf

init_db()

st.title("📚 ระบบจัดการนักเรียนและเช็คชื่อ")

menu = ["เพิ่มนักเรียน", "เช็คชื่อ", "สถิติการเช็คชื่อ"]
choice = st.sidebar.selectbox("เมนู", menu)

if choice == "เพิ่มนักเรียน":
    st.subheader("➕ เพิ่มนักเรียนใหม่")
    name = st.text_input("ชื่อนักเรียน")
    grade = st.selectbox("ระดับชั้น", ["ม.1", "ม.2", "ม.3"])
    phone = st.text_input("เบอร์โทรศัพท์")
    email = st.text_input("อีเมล")
    if st.button("บันทึก"):
        add_student(name, grade, phone, email)
        st.success("✅ บันทึกเรียบร้อย")

elif choice == "เช็คชื่อ":
    st.subheader("✅ เช็คชื่อนักเรียน")
    students = get_students()
    df = pd.DataFrame(students, columns=["ID", "ชื่อ", "ชั้น", "เบอร์โทร", "อีเมล"])
    for i, row in df.iterrows():
        if st.button(f"เช็คชื่อ: {row['ชื่อ']}", key=row["ID"]):
            mark_attendance(row["ID"])
            st.success(f"บันทึกการเช็คชื่อให้ {row['ชื่อ']}")
    st.dataframe(df)

elif choice == "สถิติการเช็คชื่อ":
    st.subheader("📊 สถิติการเช็คชื่อ")
    stats = get_attendance_stats()
    st.dataframe(stats)
    if st.button("📤 ส่งออก Excel"):
        export_excel(stats)
        st.success("✅ ส่งออก Excel สำเร็จ")
    if st.button("📄 ส่งออก PDF"):
        export_pdf(stats)
        st.success("✅ ส่งออก PDF สำเร็จ")