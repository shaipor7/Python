from fpdf import FPDF,enums

class PDF(FPDF):
    def __init__(self):
        self.name = str(input("Name: "))
        print(self.name)
        print(type(self.name))
    def header(self,name):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", center= True, align="C")
        # Performing a line break:
        self.ln(40)
        # Rendering logo:
        self.image("shirtificate.png", x=enums.Align.C , w=pdf.epw, h=pdf.epw)
        #Printing texts on shirt
        self.set_text_color(r=255, g=255, b=255)
        self.cell(30, -250, name , center= True, align="C")

pdf = PDF()
pdf.header(input("Name: "))
pdf.output("tuto1.pdf")
