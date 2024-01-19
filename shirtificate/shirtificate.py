from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         # Rendering logo:
#         self.image("shirtificate.png", 10, 8, 33)
#         # Setting font: helvetica bold 15
#         self.set_font("helvetica", "B", 15)
#         # Moving cursor to the right:
#         self.cell(80)
#         # Printing title:
#         self.cell(30, 10, "CS50 Shirtificate", align="C")
#         # Performing a line break:
#         self.ln(20)
# pdf = PDF()
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(80)
pdf.cell(40, 10, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png",h=pdf.eph, w=pdf.epw/2)
pdf.output("tuto1.pdf")
