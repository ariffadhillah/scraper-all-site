import requests
from bs4 import BeautifulSoup
import csv
import re
import os

import pandas as pd

payload = {}
headers = {
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'accept-language': 'en-US,en;q=0.9,id;q=0.8',
#   'cache-control': 'max-age=0',
  'cookie': '_ga=GA1.1.775056967.1727393498; _fbp=fb.1.1727393499047.530981323309308148; __gads=ID=14c283ea7b01c614:T=1727393498:RT=1727932285:S=ALNI_MY9GaHVzYXCQP6IOS6F4k078pTD4Q; __gpi=UID=00000f1efd883079:T=1727393498:RT=1727932285:S=ALNI_Mb0PwGNu1MpQX_rbVIZOGoWvLK_tw; __eoi=ID=eceddeef2df92e4f:T=1727393498:RT=1727932285:S=AA-AfjYrwb389Zc6u3iKnWdIo_n0; _ga_L762LW6J3N=GS1.1.1727932283.4.1.1727932344.0.0.0',
#   'dnt': '1',
#   'priority': 'u=0, i',
#   'referer': 'https://centralnymoms.com/resources/',
#   'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'same-origin',
#   'sec-fetch-user': '?1',
#   'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

response = requests.get('https://therocklandcountymoms.com/resources/doctors/',  headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

data = []

# Temukan elemen div dengan class tertentu
reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})
# print(reviews_1)
for review in reviews_1:
    title = 'Doctors & Dentists'
    paragraphs = review.find_all('p')
    
    # Loop setiap p
    for paragraph in paragraphs:
        # Ambil nama dari elemen <a> pertama jika ada
        name = ''
        if paragraph.find('a'):
            name = paragraph.find('a').get_text().strip()
            url = paragraph.find('a')['href']
        else:
            # Jika tidak ada <a>, pastikan konten pertama adalah string sebelum mengakses strip()
            first_content = paragraph.contents[0]
            if isinstance(first_content, str):
                name = first_content.strip()
            url = ''
        
        address = ''
        contact = ''
        
        
        # Loop melalui isi paragraf untuk mendapatkan alamat dan kontak
        for content in paragraph.contents:
            if isinstance(content, str):
                text = content.strip()
                if any(char.isdigit() for char in text) and '-' in text:
                    contact = text
                elif not contact and text and 'http' not in text:
                    address += text + ' '


        save_data = {
            'Title': title,
            'Name': name,
            'Address': address.strip(),
            'Contact': contact,
            'Url': url
        }
        data.append(save_data)

        # Cetak data sebagai debug
        print(f"Name: {save_data['Name']}")
        print(f"Address: {save_data['Address']}")
        print(f"URL: {save_data['Url']}")
        print()

# print(data)

# Buat DataFrame dari list data
df = pd.DataFrame(data)

# Tentukan nama folder dan buat jika belum ada
folder_name = 'Rockland County'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Simpan DataFrame ke file CSV dengan nama berdasarkan title
file_name = os.path.join(folder_name, f"{title}.csv")
df.to_csv(file_name, index=False)

print(f"Data berhasil disimpan ke '{file_name}'")




# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})
# for review in reviews_1:
#     # Temukan semua elemen <p>
#     paragraphs = review.find_all('p')

#     # Loop melalui setiap <p>
#     for paragraph in paragraphs:
#         # Inisialisasi variabel
#         title = 'Dentists'
#         name = ''
#         address = ''
#         contact = ''
#         url = ''
        
#         # Ambil semua konten dalam <p>
#         contents = paragraph.contents
        
#         # Ambil nama dari konten pertama
#         if contents and isinstance(contents[0], str):
#             name = contents[0].strip().replace('&nbsp;', ' ')
        
#         # Loop untuk mendapatkan alamat, kontak, dan URL
#         for content in contents[1:]:
#             if isinstance(content, str):
#                 text = content.strip()
#                 if any(char.isdigit() for char in text) and '-' in text:
#                     contact = text
#                 elif 'http' in text:
#                     url = text
#                 else:
#                     address += text + ' '

#         # Output hasilnya
#         print(f"name = {name}")
#         print(f"address = {address.strip()}")
#         print(f"contact = {contact}")
#         print(f"url = {url}")
#         print('')


# Misalnya, Anda sudah memiliki objek BeautifulSoup yang disebut 'soup'
# Contoh pengambilan data
# Misalnya, Anda sudah memiliki objek BeautifulSoup yang disebut 'soup'
# data = []

# # Misalnya, ini adalah hasil dari web scraping Anda
# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})
# for review in reviews_1:
#     paragraphs = review.find_all('p')

#     for paragraph in paragraphs:
#         title = 'Reading'
#         name = ''
#         address = ''
#         contact = ''
#         url = ''
        
#         contents = paragraph.contents
        
#         if contents and isinstance(contents[0], str):
#             name = contents[0].strip().replace('&nbsp;', ' ')
        
#         for content in contents[1:]:
#             if isinstance(content, str):
#                 text = content.strip()
#                 if any(char.isdigit() for char in text) and '-' in text:
#                     contact = text
#                 elif 'http' in text:
#                     url = text
#                 else:
#                     address += text + ' '

#         save_data = {
#             'title': title,
#             'name': name,
#             'address': address.strip(),
#             'contact': contact,
#             'url': url
#         }

#         data.append(save_data)

# print(data)

# # Buat DataFrame dari list data
# df = pd.DataFrame(data)

# # Tentukan nama folder dan buat jika belum ada
# folder_name = 'Central NY'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Simpan DataFrame ke file CSV dengan nama berdasarkan title
# file_name = os.path.join(folder_name, f"{title}.csv")
# df.to_csv(file_name, index=False)

# print(f"Data berhasil disimpan ke '{file_name}'")
