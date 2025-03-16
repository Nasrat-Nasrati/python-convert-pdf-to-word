import os
import pdfplumber

# Get the PDF file path from user input
pdf_path = input("Enter the PDF file path (e.g., E:/Python Projects/pdf_converter/pdf data/week2 of html.pdf): ")
output_folder = "converted_files"

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    print("Error: File not found")
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate output text file path
txt_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".txt"))

# Process the PDF and convert to text file
try:
    # Open the PDF and extract text
    with pdfplumber.open(pdf_path) as pdf:
        # Open the text file for writing
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  # Check if text exists
                    txt_file.write(text + "\n\n")  # Write text with a double newline between pages
    
    print(f"Text file created successfully: {txt_path}")
except Exception as e:
    print(f"Error: Unable to create text file: {e}")