import pandas as pd
import re

# Memuat file CSV
df = pd.read_csv('hasil---scraoing--email-Rockland County.csv')

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
df.to_csv('hasil-hasil---scraoing--email-Rockland County.csv', index=False)

print("Nomor telepon berhasil diekstrak dan disimpan!")
