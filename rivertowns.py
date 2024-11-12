import requests
from bs4 import BeautifulSoup
import csv
import re
import os

import pandas as pd

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'accept-language': 'en-US,en;q=0.9,id;q=0.8',
#   'cache-control': 'max-age=0',
#   'cookie': '_ga=GA1.1.943830747.1727881041; _fbp=fb.1.1727881041447.974084567846443213; __gads=ID=f36d53fee26cce66:T=1727881042:RT=1727914690:S=ALNI_MarIkKYZSi85T0ZwT2ckli_0bJriQ; __gpi=UID=00000f2ef67a43fb:T=1727881042:RT=1727914690:S=ALNI_MaomqhYhUhLvzR11T4W-RVIGaMiQw; __eoi=ID=8c8ca9b75df51370:T=1727881042:RT=1727914690:S=AA-AfjZA8sC5fXNNKzy5KZt_suTR; cf_chl_rc_m=1; cf_clearance=y6MldS9oq7UWiiGxKi1j0OU6MapRJ.wQvHF5wuNU8uw-1727914852-1.2.1.1-hB7gx2gEwiXedHh_Aja6jVRUnkClVFn3rTM5LF4kpNp5iEPs0eXbuunMUl5N6WjUgyfC2f6UkeiGsSLqJVV8Hv27y25wmS3VzsIMIP6twyeJV4TpYFzwDcA52spmy823YZJtFHR87R3r40StuKWFa8wEqeOp2N96_QFgQ9tC4mpojJFkg3DRZjT83dAaKRiWsspGNzytdPejTnflRcGaz4d__61G52XtOk1BS0Bgf1E9O5CDpzJNwAVjJT..a5uN8RlqFqPi1mTQbT53z.gDGmfUBu2BdAFLC2GZ3vmO2K6NwgVG3xroiwDF7OYPvj5TksOYtH.1fdjIgAF7pV2e2KdPCqO4u607ci5cZ8SGgylYJCqbOjUjIzwrz2HEOJ9pwAO0OlS7PLEKnvEWhvehNG9f8qta0Wx66.vohaHTPQU; _ga_96MDJBENSY=GS1.1.1727912936.3.1.1727914861.0.0.0; _ga_WNFDMLR16W=GS1.1.1727912936.6.1.1727914862.0.0.0',
# #   'dnt': '1',
# #   'priority': 'u=0, i',
#   'referer': 'https://therocklandcountymoms.com/resources/bookstores/',
# #   'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'same-origin',
#   'sec-fetch-user': '?1',
#   'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}


response = requests.get('https://huntingtonsmithtownmoms.com/resources/parties-and-events/',  headers=headers)

# Membuat objek BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Temukan semua div dengan kelas et_pb_tab_content
reviews_1 = soup.find_all('div', {'class': 'entry-content'})
print(reviews_1)
# print(reviews_1)

# # # Inisialisasi list untuk menyimpan data yang diekstrak
# data_list = []

# # Definisikan variabel title di luar loop
# title = 'Book Stores'

# # Iterasi melalui setiap elemen div.et_pb_tab_content
# for review in reviews_1:
#     # Cari semua elemen <a> untuk mengambil nama dan url
#     a_tags = review.find_all('a')
    
#     for a_tag in a_tags:
#         # Nama bisnis
#         name = a_tag.get_text(strip=True)
        
#         # URL bisnis
#         url = a_tag['href']
        
#         # Temukan elemen berikutnya (alamat)
#         address = a_tag.find_next('p').get_text(strip=True)
        
#         # Temukan elemen berikutnya setelah alamat (nomor kontak)
#         contact = a_tag.find_next('p').find_next('p').get_text(strip=True)
        
#         # Gabungkan alamat dan kontak
#         add = address + ' ' + contact
        
#         # Simpan hasilnya dalam dict
#         data_save = {
#             'Title': title,
#             'Name': name,
#             'Address': add.replace(name, '').strip(),
#             'Url': url
#         }
        
#         # Tambahkan ke dalam list
#         data_list.append(data_save)

#         # Cetak data sebagai debug
#         print(f"Name: {data_save['Name']}")
#         print(f"Address: {data_save['Address']}")
#         print(f"URL: {data_save['Url']}")
#         print()

# # # Buat DataFrame dari list data
# df = pd.DataFrame(data_list)

# # Tentukan nama folder dan buat jika belum ada
# folder_name = 'Rockland County'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Simpan DataFrame ke file CSV dengan nama berdasarkan title
# file_name = os.path.join(folder_name, f"{title}.csv")
# df.to_csv(file_name, index=False)

# print(f"Data berhasil disimpan ke '{file_name}'")