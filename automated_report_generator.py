from fpdf import FPDF
import pandas as pd

# Step 1: Read data
data = pd.read_csv('sample_data.csv')

# Step 2: Analyze data
summary = data.describe()

# Step 3: Create PDF report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Automated Data Analysis Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font('Courier', '', 10)

pdf.cell(0, 10, 'Summary of CSV Data:', ln=True)

for line in summary.to_string().split('\n'):
    pdf.cell(0, 8, line, ln=True)

pdf.output('automated_report.pdf')

print(\"✅ Report generated: automated_report.pdf\")
