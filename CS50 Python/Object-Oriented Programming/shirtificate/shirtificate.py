from fpdf import FPDF
from fpdf import Align

class File:
    def __init__(self, name):
        self.name = name

    def create_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", "B", 30)
        pdf.cell(0, 40, "CS50 Shirtificate", center=True, align="C")
        pdf.image("shirtificate.png", x=Align.C, y=60, h=180, w=180)
        pdf.set_font("times", "B", 25)
        pdf.set_text_color(255)
        pdf.cell(0, 210, f"{self.name} took CS50", center=True, align="C")
        pdf.output("shirtificate.pdf")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name



def main():
    file = File(input("Name: "))
    file.create_pdf()

if __name__ == "__main__":
    main()
