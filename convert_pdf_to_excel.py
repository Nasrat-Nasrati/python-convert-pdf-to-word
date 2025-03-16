import os
import pdfplumber
import pandas as pd

# Get the PDF file path from user input
pdf_path = input("Enter the PDF file path (e.g., E:/Python Projects/pdf_converter/pdf data/week2 of html.pdf): ")
output_folder = "converted_files"

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    print("Error: File not found")
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate output Excel file path
excel_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".xlsx"))

# Process the PDF and convert to Excel
try:
    # List to store text from each page
    text_data = []
    
    # Open the PDF and extract text
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # Check if text exists
                text_data.append([text])  # Add text as a single column entry
    
    # Create a DataFrame with the text data
    df = pd.DataFrame(text_data, columns=["Page Text"])
    
    # Save the DataFrame to an Excel file
    df.to_excel(excel_path, index=False)
    print(f"Excel file created successfully: {excel_path}")
except Exception as e:
    print(f"Error: Unable to create Excel file: {e}")