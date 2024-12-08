import pandas as pd
import re

# Load the CSV file
file_path = 'Doctors Dentists.csv'  # Replace with your actual file name
df = pd.read_csv(file_path)

# Fungsi untuk mengekstrak email
def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

# Fungsi untuk mengekstrak nomor telepon
def extract_contact(text):
    contact_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    matches = re.findall(contact_pattern, text)
    # Tambahkan tanda petik satu di awal setiap nomor
    return '\n'.join([f"'{match.strip()}" for match in matches]) if matches else None

# Fungsi untuk menghapus email dan nomor kontak dari kolom Address
def remove_email_and_contact(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    contact_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    text = re.sub(email_pattern, '', text)  # Hapus email
    text = re.sub(contact_pattern, '', text)  # Hapus nomor kontak
    return text.strip()

# Ekstrak email dan nomor kontak ke kolom baru
df['Email'] = df['Address'].apply(lambda x: extract_email(x) if pd.notnull(x) else None)
df['Contact'] = df['Address'].apply(lambda x: extract_contact(x) if pd.notnull(x) else None)

# Hapus email dan nomor kontak dari kolom Address
df['Address'] = df['Address'].apply(lambda x: remove_email_and_contact(x) if pd.notnull(x) else None)


# Save the modified DataFrame to a new CSV file
output_file_path = '__cleaned_data_Doctors Dentists.csv'
df.to_csv(output_file_path, index=False)

print("Phone numbers have been extracted into 'number_phone' and removed from 'Address'.")
print(f"Cleaned data saved to '{output_file_path}'.")
