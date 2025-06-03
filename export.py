import pandas as pd

def export_excel(data):
    df = pd.DataFrame(data, columns=["ชื่อ", "ชั้น", "จำนวนครั้งที่มาเรียน"])
    df.to_excel("attendance_report.xlsx", index=False)

def export_pdf(data):
    # ตัวอย่างง่าย ๆ สร้าง PDF โดยแปลงตารางเป็น HTML แล้วเซฟ
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 3  # แบ่งสามคอลัมน์เท่า ๆ กัน

    pdf.cell(0, 10, "รายงานสถิติการเช็คชื่อ", ln=True, align="C")

    headers = ["ชื่อ", "ชั้น", "จำนวนครั้งที่มาเรียน"]
    for header in headers:
        pdf.cell(col_width, line_height, header, border=1)
    pdf.ln(line_height)

    for row in data:
        for item in row:
            pdf.cell(col_width, line_height, str(item), border=1)
        pdf.ln(line_height)

    pdf.output("attendance_report.pdf")
