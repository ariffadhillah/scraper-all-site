# import pandas as pd

# # Membaca kedua file CSV
# df1 = pd.read_csv('New folder/data_hasil-New York-2.csv')
# df2 = pd.read_csv('New folder/data_hasil-New York-2.csv')

# # Menggabungkan kedua DataFrame berdasarkan kolom 'URL'
# df_merged = pd.merge(df1, df2[['url', 'Email']], on='url', how='left', suffixes=('_1', '_2'))

# # Mengisi kolom email di df1 dengan email dari df2 jika kosong
# df_merged['email_1'] = df_merged.apply(lambda row: row['email_2'] if pd.isna(row['email_1']) or row['email_1'] == '' else row['email_1'], axis=1)

# # Menghapus kolom email dari df2 setelah digabungkan
# df_merged = df_merged.drop(columns=['email_2'])

# # Menyimpan hasil ke file CSV baru
# df_merged.to_csv('New folder/data_hasil-New York-1_updated.csv', index=False)



import pandas as pd

# Membaca kedua file CSV
df1 = pd.read_csv('New folder/data_hasil-New York-1.csv')
df2 = pd.read_csv('New folder/data_hasil-New York-2.csv')


# Menggabungkan kedua DataFrame berdasarkan kolom 'url'
df_merged = pd.merge(df1, df2[['url', 'Email']], on='url', how='left', suffixes=('', '_from_file2'))

# Mengisi kolom email di df1 dengan email dari df2 jika kosong
df_merged['Email'] = df_merged.apply(lambda row: row['Email_from_file2'] if pd.isna(row['Email']) or row['Email'] == '' else row['Email'], axis=1)

# Menghapus kolom email dari df2 setelah digabungkan
df_merged = df_merged.drop(columns=['Email_from_file2'])

# Menyimpan hasil ke file CSV baru
df_merged.to_csv('New folder/data_hasil-New York-1_updated.csv', index=False)
