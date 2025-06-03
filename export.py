import pandas as pd
from fpdf import FPDF

def export_excel(data):
    df = pd.DataFrame(data, columns=["ชื่อ", "ชั้น", "จำนวนครั้งที่มาเรียน"])
    df.to_excel("attendance_report.xlsx", index=False)

def export_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="รายงานการเช็คชื่อ", ln=1, align="C")
    for row in data:
        pdf.cell(200, 10, txt=f"{row[0]} | {row[1]} | {row[2]} ครั้ง", ln=1)
    pdf.output("attendance_report.pdf")