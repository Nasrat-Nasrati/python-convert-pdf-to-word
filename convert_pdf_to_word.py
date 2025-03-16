import os
import pdfplumber
from docx import Document

# Get the PDF file path from user input
pdf_path = input("Enter the PDF file path (e.g., E:/Python Projects/pdf_converter/pdf data/week2 of html.pdf): ")
output_folder = "converted_files"

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    print("Error: File not found")
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate output Word file path
word_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".docx"))

# Process the PDF and convert to Word
try:
    doc = Document()
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # Check if text exists to avoid adding empty paragraphs
                doc.add_paragraph(text)
    doc.save(word_path)
    print(f"Word file created successfully: {word_path}")
except Exception as e:
    print(f"Error: Unable to create Word file: {e}")