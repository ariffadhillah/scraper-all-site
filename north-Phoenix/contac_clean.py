import pandas as pd
import re

# Load the CSV file
file_path = 'hasil-scraping---1.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Define a function to extract phone numbers
def extract_phone_number(text):
    # Regular expression to match phone numbers
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None

# Apply the function to the 'address' column and store the result in 'number_phone' column
df['Contact'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# Opsional, menghapus nomor telepon dari kolom 'Address'
df['Address'] = df['Address'].apply(lambda x: re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '', x).strip() if isinstance(x, str) else x)

# Save the modified DataFrame to a new CSV file
output_file_path = 'cleaned_data_____.csv'
df.to_csv(output_file_path, index=False)

print("Phone numbers have been extracted and saved to a new column in cleaned_data.csv.")

