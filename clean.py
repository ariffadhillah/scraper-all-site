import pandas as pd

# Membaca file CSV
df = pd.read_csv('New folder/New York--1.csv')

# Menghapus huruf "n" yang hanya terdiri dari satu huruf pada kolom email
df['Email'] = df['Email'].apply(lambda x: '' if x == 'n' else x)

# Menyimpan perubahan ke file CSV baru
df.to_csv('New folder/data_hasil-New York-2.csv', index=False)




# import pandas as pd

# # Membaca file CSV
# df = pd.read_csv('file_bersih.csv')

# # Menghapus baris dengan email yang duplikat, hanya mempertahankan yang pertama,
# # dan mempertahankan baris dengan kolom email kosong
# df_clean = df[df['Email'] != ''].drop_duplicates(subset='Email', keep='first')

# # Menggabungkan kembali dengan baris yang kosong di kolom email
# df_clean = pd.concat([df_clean, df[df['Email'] == '']])

# # Menyimpan perubahan ke file CSV baru
# df_clean.to_csv('clean_bersih.csv', index=False)



# import pandas as pd

# # Membaca file CSV
# df = pd.read_csv('file_bersih.csv')

# # Memisahkan baris yang kosong di kolom email
# empty_emails = df[df['Email'].isna() | (df['Email'] == '')]

# # Menghapus duplikat hanya untuk baris yang memiliki email, bukan yang kosong
# df_non_empty = df[df['Email'].notna() & (df['Email'] != '')].drop_duplicates(subset='Email', keep='first')

# # Menggabungkan kembali baris dengan email kosong
# df_clean = pd.concat([df_non_empty, empty_emails])

# # Menyimpan perubahan ke file CSV baru
# df_clean.to_csv('data_clean.csv', index=False)
