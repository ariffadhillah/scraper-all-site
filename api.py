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
  'cookie': '_ga=GA1.1.1660840709.1727393440; _fbp=fb.1.1727393440750.242359093645653057; cf_clearance=Dion7Ia5tc2XgXlg1HiEb2bYdKF7..I3N_h2Fl0sK5U-1727861928-1.2.1.1-kiJGKgmnAsvSVKzhRhAkl7hattn4NK2mIypJJqL9a4Hh4K.TvK18pzd1waLLRU6v.aIfKXYMUILwJx1jB98Z1Kae6Z4SFxsadVUvPd9KpgNw8aONj0.69gVLtxrSR8ExcVy01FLN1MZtnV02gOF71lKRDrR5ghwIC.al74SALvsGW4A.Pg_PHdZv__3uqdaM4hTcTYykeRr8kAVcdLE3TtEBrHmEVc6u73ndgYBkcTK0esphnu81nrTPfB3NDTXHPtfWHa4KH36MEBxilX_RNFgp27JaujE.gK91Jte1yIsaOqMhMjKe76G0tkFnTHjUhPCsJCXkVEnailE4.2d5PMxXesxO0rGeysa9lKmoqXy310YT7yqxux_iTZuifPi4ZEUtaMcHdrhd2MbTx9bxt3uJANGCwI8pUpM_N1hd_3E; __gads=ID=77b525b2689d8115:T=1727393441:RT=1727861939:S=ALNI_Majj9ac-EzCGXrbbF7EaBSlaZrp_w; __gpi=UID=00000f065da44163:T=1727393441:RT=1727861939:S=ALNI_MY17Zqw2DtcdAf9x47ushPoYXPMZg; __eoi=ID=35da3b83d5e60587:T=1727393441:RT=1727861939:S=AA-AfjbALMDFSCtcaXuWp7_mh3AN; _ga_96MDJBENSY=GS1.1.1727861937.2.1.1727861951.0.0.0; _ga_WNFDMLR16W=GS1.1.1727861938.2.1.1727861951.0.0.0',
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


response = requests.get('https://capitaldistrictmoms.com/resources/aquatics/',  headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')



# Temukan semua elemen <div> dengan class 'et_pb_toggle_content clearfix'
reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})
# print(reviews_1)
# Inisialisasi list untuk menyimpan data
data = []

# fields = ['Title', 'Name', 'Contact', 'Address', 'Url']
# filename = ' .csv'

for review in reviews_1:
    p_tags = review.find_all('p') 
    for p_tag in p_tags:
        title = 'Doctors & Dentists'
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
            
            # # Mencari elemen yang mengandung teks "Phone" dengan mengabaikan spasi
            # phone_element = p_tag.find(string=re.compile(r'^\s*Contact:\s*'))

            # if phone_element:
            #     # Temukan sibling berikutnya setelah elemen "Phone:"
            #     phone_number = phone_element.find_next(string=True).strip()
            #     # print(f"Phone: {phone_number}")
            # else:
            #     print("Phone element not found in this <p>.")


            # Mencari alamat dalam <p> yang sama (asumsi alamat ada di <p> yang sama)
            # address = p_tag.get_text(strip=True).replace('Phone:', '').strip()
            address = p_tag.get_text(strip=True).strip()
            print(address)
            # print(f"Address: {address}")
            # print()

        else:
            print("Tidak ada elemen <a> di dalam <p>")

        # print(name)
        data_save = {
            'Title': title,
            'Name' : name, 
            'Address' : address.replace(name, ''),
            'Url' : url           
        }
        data.append(data_save)
        print(data_save['Name'])
        print(data_save['Address'])
        print(data_save['Url'])
        print()


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



