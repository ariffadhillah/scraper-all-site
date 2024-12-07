import pandas as pd
import re

# Load the CSV file
file_path = '_________hasil-scraping.csv'  # Replace with your actual file name
df = pd.read_csv(file_path)

# Define a function to extract phone numbers and format them with a single quote
def extract_phone_number(text):
    # Regular expression to match different phone number formats
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}(?:\s?\d+)?'
    matches = re.findall(phone_pattern, text)
    # Format each phone number with a single quote
    return '\n'.join([f"'{match.strip()}" for match in matches]) if matches else None

# Define a function to remove phone numbers from the text
def remove_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}(?:\s?\d+)?'
    return re.sub(phone_pattern, '', text).strip()

# Extract phone numbers into the 'number_phone' column
df['Contact'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# Remove phone numbers from the 'Address' column
df['Address'] = df['Address'].apply(lambda x: remove_phone_numbers(x) if pd.notnull(x) else None)

# Save the modified DataFrame to a new CSV file
output_file_path = 'cleaned_data.csv'
df.to_csv(output_file_path, index=False)

print("Phone numbers have been extracted into 'number_phone' and removed from 'Address'.")
print(f"Cleaned data saved to '{output_file_path}'.")