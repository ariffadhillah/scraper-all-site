# import pandas as pd

# # Membaca kedua file CSV
# file_pertama = pd.read_csv('data-1.csv')
# file_kedua = pd.read_csv('data-2.csv')

# # Periksa nama kolom
# print("Kolom di file pertama:", file_pertama.columns)
# print("Kolom di file kedua:", file_kedua.columns)

# # Menggabungkan data berdasarkan kolom 'Name'
# merged_data = file_pertama.merge(file_kedua, on='Name', how='left', suffixes=('_pertama', '_kedua'))

# # Periksa nama kolom setelah merge
# print("Kolom di merged_data:", merged_data.columns)

# # Mengisi email yang kosong di file pertama dengan email dari file kedua
# merged_data['Email'] = merged_data['Email_pertama'].combine_first(merged_data['Email_kedua'])

# # Memilih hanya kolom yang diperlukan untuk file akhir
# final_data = merged_data[['County_pertama', 'Title_pertama', 'Name', 'Address_pertama', 'Contact_pertama', 'Email', 'Url_pertama']]

# # Mengganti nama kolom ke bentuk sederhana
# final_data.rename(columns={
#     'County_pertama': 'County',
#     'Title_pertama': 'Title',
#     'Address_pertama': 'Address',
#     'Contact_pertama': 'Contact',
#     'Url_pertama': 'Url'
# }, inplace=True)

# # Menyimpan hasil ke file CSV baru
# final_data.to_csv('hasil.csv', index=False)

# print("Email yang kosong telah diisi, hasilnya disimpan di 'hasil.csv'")




import pandas as pd

# Membaca kedua file CSV
# file_pertama = pd.read_csv('hasil-sacrpingNew York -- email - Sheet1-2.csv')
# file_kedua = pd.read_csv('hasil-sacrpingNew York -- email - Sheet1-2.csv')
file_pertama = pd.read_csv('data-1.csv')
file_kedua = pd.read_csv('data-2.csv')

# Periksa nama kolom
print("Kolom di file pertama:", file_pertama.columns)
print("Kolom di file kedua:", file_kedua.columns)

# Menggabungkan data berdasarkan kolom 'Name'
merged_data = file_pertama.merge(file_kedua, on='Name', how='left', suffixes=('_pertama', '_kedua'))

# Periksa nama kolom setelah merge
print("Kolom di merged_data:", merged_data.columns)

# Mengisi email yang kosong di file pertama dengan email dari file kedua
merged_data['Email'] = merged_data['Email_pertama'].combine_first(merged_data['Email_kedua'])

# Memilih hanya kolom yang diperlukan untuk file akhir
final_data = merged_data[['County_pertama', 'Title_pertama', 'Name', 'Address_pertama', 'Contact_pertama', 'Email', 'Url_pertama']]

# Mengganti nama kolom ke bentuk sederhana
final_data.rename(columns={
    'County_pertama': 'County',
    'Title_pertama': 'Title',
    'Address_pertama': 'Address',
    'Contact_pertama': 'Contact',
    'Url_pertama': 'Url'
}, inplace=True)

# Menghapus duplikat berdasarkan kolom 'Name'
final_data = final_data.drop_duplicates(subset=['Name'], keep='first')

# Menyimpan hasil ke file CSV baru
final_data.to_csv('hasil.csv', index=False)

print("Email yang kosong telah diisi dan duplikat dihapus, hasilnya disimpan di 'hasil.csv'")
