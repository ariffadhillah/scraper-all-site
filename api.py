import requests
from bs4 import BeautifulSoup
import csv
import re
import os

import pandas as pd

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,id;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': '_fbp=fb.1.1727272428520.180776536776397540; _gid=GA1.2.9552882.1727491641; _gat=1; _ga_96MDJBENSY=GS1.1.1727512606.12.1.1727512714.0.0.0; _ga=GA1.2.745235258.1727272423; _ga_R93DRXD5SF=GS1.2.1727512612.10.1.1727512715.0.0.0',
  'dnt': '1',
  'priority': 'u=0, i',
  'referer': 'https://centralnymoms.com/resources/',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}


response = requests.get('https://northernwestchestermoms.com/resources/attractions/',  headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')



# Temukan semua elemen <div> dengan class 'et_pb_toggle_content clearfix'
reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})

# Inisialisasi list untuk menyimpan data
data = []

# fields = ['Title', 'Name', 'Contact', 'Address', 'Url']
# filename = ' .csv'

for review in reviews_1:
    p_tags = review.find_all('p') 
    for p_tag in p_tags:
        title = ' '
        name = ''
        phone_number = ''
        address = ''
        url = ''
        a_tag = p_tag.find('a')  
        if a_tag:
            name = a_tag.get_text(strip=True) 
            url = a_tag.get('href')  
            # print(f"name = {name}")
            # print(f"url = {url}")
            
            # Mencari elemen yang mengandung teks "Phone" dengan mengabaikan spasi
            phone_element = p_tag.find(string=re.compile(r'^\s*Phone:\s*'))

            if phone_element:
                # Temukan sibling berikutnya setelah elemen "Phone:"
                phone_number = phone_element.find_next(string=True).strip()
                # print(f"Phone: {phone_number}")
            else:
                print("Phone element not found in this <p>.")


            # Mencari alamat dalam <p> yang sama (asumsi alamat ada di <p> yang sama)
            address = p_tag.get_text(strip=True).replace('Phone:', '').strip()
            # print(f"Address: {address}")
            # print()

        else:
            print("Tidak ada elemen <a> di dalam <p>")

        print(name)
        data_save = {
            'Title': title,
            'Name' : name, 
            'Contact' : '',
            'Address' : address.replace(name, ''),
            'Url' : url           
        }
        data.append(data_save)


# Buat DataFrame dari list data
df = pd.DataFrame(data)

# Tentukan nama folder dan buat jika belum ada
folder_name = 'Greater Rochester'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Simpan DataFrame ke file CSV dengan nama berdasarkan title
file_name = os.path.join(folder_name, f"{title}.csv")
df.to_csv(file_name, index=False)

print(f"Data berhasil disimpan ke '{file_name}'")
      



