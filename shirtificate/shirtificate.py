from fpdf import FPDF,enums

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(40)
        # Rendering logo:
        self.image("shirtificate.png", x=enums.Align.C , w=pdf.epw, h=pdf.epw)
        # Moving cursor to the right:
        self.cell(80)
        self.cell(30, -250, "CS50 Shirtificate", align="C")
pdf = PDF()
pdf.output("tuto1.pdf")
