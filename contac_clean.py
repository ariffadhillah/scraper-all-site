import pandas as pd
import re

# Memuat file CSV
df = pd.read_csv('Sound Shore Moms-----.csv')

# Fungsi untuk mengekstrak nomor telepon
def extract_phone(address):
    if isinstance(address, str):  # Pastikan alamat adalah string
        phone_match = re.search(r'\(\d{3}\) \d{3}-\d{4}', address)
        return phone_match.group() if phone_match else ''
    return ''  # Kembalikan string kosong jika alamat bukan string

# Terapkan fungsi pada kolom 'Address'
df['Phone Number'] = df['Address'].apply(extract_phone)

# Opsional, menghapus nomor telepon dari kolom 'Address'
df['Address'] = df['Address'].apply(lambda x: re.sub(r'\(\d{3}\) \d{3}-\d{4}', '', x).strip() if isinstance(x, str) else x)

# Simpan hasil ke file CSV yang diperbarui
df.to_csv('Sound Shore Moms-------------------.csv', index=False)

print("Nomor telepon berhasil diekstrak dan disimpan!")




# import pandas as pd
# import re

# # Load the CSV file
# file_path = 'Rye  Rye Brook.csv'  # Replace with your actual file path
# df = pd.read_csv(file_path)

# # Define a function to extract phone numbers
# def extract_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     match = re.search(phone_pattern, text)
#     return match.group(0) if match else None

# # Apply the function to the 'address' column and store the result in 'number_phone' column
# df['number_phone'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# # Save the modified DataFrame to a new CSV file
# output_file_path = 'cleaned_data_____.csv'
# df.to_csv(output_file_path, index=False)

# print("Phone numbers have been extracted and saved to a new column in cleaned_data.csv.")



# import pandas as pd
# import re

# # Load the CSV file
# file_path = 'Rye  Rye Brook.csv'  # Replace with your actual file path
# df = pd.read_csv(file_path)

# # Define a function to extract phone numbers
# def extract_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     match = re.search(phone_pattern, text)
#     return match.group(0) if match else None

# # Define a function to remove phone numbers from text
# def remove_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     return re.sub(phone_pattern, '', text)

# # Extract phone numbers into a new 'number_phone' column
# df['number_phone'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# # Remove phone numbers from the 'address' column
# df['Address'] = df['Address'].apply(lambda x: remove_phone_number(x) if pd.notnull(x) else None)

# # Save the modified DataFrame to a new CSV file
# output_file_path = 'cleaned_data_no_phone_in_address.csv'
# df.to_csv(output_file_path, index=False)

# print("Phone numbers have been extracted, saved in 'number_phone', and removed from 'address' in cleaned_data_no_phone_in_address.csv.")



# import pandas as pd
# import re

# # Load the CSV file
# file_path = 'Sayville Patchogue Area.csv'  # Replace with your actual file path
# df = pd.read_csv(file_path)

# # Define a function to extract phone numbers
# def extract_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     match = re.search(phone_pattern, text)
#     # Add single quote at the beginning if phone number is found
#     return f"'{match.group(0)}" if match else None

# # Define a function to remove phone numbers from text
# def remove_phone_number(text):
#     # Regular expression to match phone numbers
#     phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
#     return re.sub(phone_pattern, '', text)

# # Extract phone numbers into a new 'number_phone' column with a single quote at the beginning
# df['number_phone'] = df['Address'].apply(lambda x: extract_phone_number(x) if pd.notnull(x) else None)

# # Remove phone numbers from the 'Address' column
# df['Address'] = df['Address'].apply(lambda x: remove_phone_number(x) if pd.notnull(x) else None)

# # Save the modified DataFrame to a new CSV file
# output_file_path = 'Sayville Patchogue Area______________.csv'
# df.to_csv(output_file_path, index=False)

# print("Phone numbers have been extracted, prefixed with a single quote in 'number_phone', and removed from 'Address' in cleaned_data_no_phone_in_address.csv.")
