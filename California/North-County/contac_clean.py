# import pandas as pd
# import re

# # Load the CSV file
# file_path = '_________hasil-scraping.csv'  # Replace with your actual file name
# df = pd.read_csv(file_path)

# # Define a function to extract phone numbers and format them with a single quote
# def extract_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[.\s-]?\d{3}[.\s-]?\d{4}\b'
#     matches = re.findall(phone_pattern, text)
#     # Format each phone number with a single quote and normalize separators to '-'
#     return ', '.join([f"'{match.replace('.', '-').replace(' ', '-').replace('--', '-')}" for match in matches]) if matches else None

# # Define a function to remove phone numbers from the text
# def remove_phone_numbers(text):
#     phone_pattern = r'\b\d{3}[.\s-]?\d{3}[.\s-]?\d{4}\b'
#     return re.sub(phone_pattern, '', text).strip(", ").strip()

# # Extract phone numbers into the 'number_phone' column
# df['Contact'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# # Remove phone numbers from the 'Address' column
# df['Address'] = df['Address'].apply(lambda x: remove_phone_numbers(x) if pd.notnull(x) else None)

# # Save the modified DataFrame to a new CSV file
# output_file_path = 'cleaned_data__tambahan_________hasil-scraping.csv'
# df.to_csv(output_file_path, index=False)

# print("Phone numbers have been extracted into 'Contact' and removed from 'Address'.")
# print(f"Cleaned data saved to '{output_file_path}'.")




import pandas as pd
import re

# Data input (ganti dengan file CSV Anda)
file_path = '_________hasil-scraping.csv'  # Replace with your actual file path
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
df['email_1'] = df['Address'].apply(lambda x: extract_email(x) if pd.notnull(x) else None)
df['Contact'] = df['Address'].apply(lambda x: extract_contact(x) if pd.notnull(x) else None)

# Hapus email dan nomor kontak dari kolom Address
df['Address'] = df['Address'].apply(lambda x: remove_email_and_contact(x) if pd.notnull(x) else None)

# Simpan hasil ke file CSV baru
output_file_path = 'cleaned_data_with_email_and_contact.csv'
df.to_csv(output_file_path, index=False)

print("Email dan nomor kontak telah diekstrak ke kolom 'email' dan 'Contact'.")
print(f"Data yang sudah dibersihkan disimpan ke '{output_file_path}'.")
