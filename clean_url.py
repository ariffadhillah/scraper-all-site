import pandas as pd

# Membaca file CSV yang sudah di-update
df = pd.read_csv('New folder/data_hasil-New York-1_updated.csv')

# Menghapus baris yang memiliki duplikat pada kolom 'url'
df_clean = df.drop_duplicates(subset='url', keep='first')

# Menyimpan hasil ke file CSV baru
df_clean.to_csv('New folder/data_hasil-New York-1_final.csv', index=False)
