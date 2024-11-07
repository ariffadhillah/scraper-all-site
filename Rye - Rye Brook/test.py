# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import os

# import pandas as pd

# payload = {}
# headers = {
# #   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #   'accept-language': 'en-US,en;q=0.9,id;q=0.8',
# #   'cache-control': 'max-age=0',
#   'cookie': '_ga=GA1.1.1286885114.1730848589; _fbp=fb.1.1730848590396.678317006908567812; __gads=ID=a9052a678395253f:T=1727359375:RT=1730853233:S=ALNI_MYMI3OwPdyNT3A6OXf87PvQVlktZw; __gpi=UID=00000f1ec8cd3344:T=1727359375:RT=1730853233:S=ALNI_Ma6iBkctqikPBCNAo9mpEHzpK-fTg; __eoi=ID=09f425c77120882a:T=1727359375:RT=1730853233:S=AA-AfjY9ZQgcxyDzUJcb09UEd3VZ; _ga_96MDJBENSY=GS1.1.1730851245.2.1.1730853253.0.0.0; _ga_V4285DGDFN=GS1.1.1730851245.8.1.1730853255.0.0.0',
# #   'dnt': '1',
# #   'priority': 'u=0, i',
# #   'referer': 'https://centralnymoms.com/resources/',
# #   'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
# #   'sec-ch-ua-mobile': '?0',
# #   'sec-ch-ua-platform': '"Windows"',
# #   'sec-fetch-dest': 'document',
# #   'sec-fetch-mode': 'navigate',
# #   'sec-fetch-site': 'same-origin',
# #   'sec-fetch-user': '?1',
# #   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
# }


# response = requests.get('https://ryeandryebrookmoms.com/activities/',  headers=headers)

# soup = BeautifulSoup(response.content, 'html.parser')



# # Temukan semua elemen <div> dengan class 'et_pb_toggle_content clearfix'
# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})
# # print(reviews_1)
# # Inisialisasi list untuk menyimpan data
# data = []

# # fields = ['Title', 'Name', 'Contact', 'Address', 'Url']
# # filename = ' .csv'

# # Iterasi melalui setiap elemen div.et_pb_tab_content
# title = 'ACTIVITIES'
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
#         data.append(data_save)

#         # Cetak data sebagai debug
#         print(f"Name: {data_save['Name']}")
#         print(f"Address: {data_save['Address']}")
#         print(f"URL: {data_save['Url']}")
#         print()

# # Buat DataFrame dari list data
# df = pd.DataFrame(data)

# # Tentukan nama folder dan buat jika belum ada
# folder_name = 'Rye - Rye Brook'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Simpan DataFrame ke file CSV dengan nama berdasarkan title
# file_name = os.path.join(folder_name, f"{title}.csv")
# df.to_csv(file_name, index=False)

# print(f"Data berhasil disimpan ke '{file_name}'")





# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # import re
# # import os 

# # # Function to process paragraphs and extract name, url, and address
# # def extract_info(paragraphs):
# #     results = []
# #     for p in paragraphs:
# #         strong_tag = p.find('strong')
# #         a_tag = p.find('a')
# #         em_tag = p.find('em')

# #         # Extract name, URL, and address based on tags
# #         if strong_tag and a_tag:
# #             name = strong_tag.text.strip()
# #             url = a_tag['href']
# #             address = em_tag.text.strip() if em_tag else p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
# #             address = address.split('for more information.')[0].strip()

# #             results.append({
# #                 'name': name,
# #                 'url': url,
# #                 'address': address
# #             })

# #         elif a_tag:  # For cases where only <a> tag is found
# #             name = a_tag.text
# #             url = a_tag['href']
# #             address = p.get_text(strip=True).replace(name, '').strip() or 'none'

# #             results.append({
# #                 'name': name,
# #                 'url': url,
# #                 'address': address
# #             })

# #     return results

# # # Fetch the webpage
# # cookies = {
# #     '_fbp': 'fb.1.1727272184560.436269777395599014',
# #     '_ga': 'GA1.2.2085893758.1727272183',
# #     # Add other necessary cookies here
# # }

# # headers = {
# #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
# # }

# # response = requests.get('https://ryeandryebrookmoms.com/activities/', cookies=cookies, headers=headers)
# # soup = BeautifulSoup(response.content, 'html.parser')

# # # Process all reviews dynamically
# # # all_reviews = soup.find_all('div', {'class': 'et_pb_text_inner'})
# # all_reviews = soup.find_all('div', class_=['et_pb_tab_content'])

# # final_results = []
# # for i, review in enumerate(all_reviews):
# #     paragraphs = review.find_all('p')
# #     result = extract_info(paragraphs)
# #     final_results.extend(result)


# # title = "Attractions"

# # for result in final_results:
# #     result['Title'] = title 

# # safe_title = re.sub(r'[^\w\s-]', '-', title).replace(' ', '-')

# # # Buat folder jika belum ada
# # folder_name = 'Northern Westchester'
# # if not os.path.exists(folder_name):
# #     os.makedirs(folder_name)

# # # Simpan data ke file CSV dengan nama berdasarkan title di dalam folder
# # csv_file = f'{folder_name}/{safe_title}.csv'  # Gunakan '/' untuk pemisah folder
# # csv_columns = ['Title', 'name', 'url', 'address']
# # try:
# #     with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
# #         writer = csv.DictWriter(file, fieldnames=csv_columns)
# #         writer.writeheader()
# #         writer.writerows(final_results)

# #     print(f"Data berhasil disimpan ke '{csv_file}'")

# # except IOError:
# #     print("Terjadi kesalahan saat menyimpan file.")


# # for result in final_results:
# #     print(f"Title = {result['Title']}")  
# #     print(f"name = {result['name']}")
# #     print(f"url = {result['url']}")
# #     print(f"address = {result['address']}")
# #     print() 






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

response = requests.get('https://ryeandryebrookmoms.com/resources/babysitting-nannies-pet-care/',  headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

data = []

fields = ['Title', 'Name', 'Address']
filename = 'BABYSITTING, NANNIES & PET CARE.csv'

# # Temukan elemen div dengan class tertentu
# reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})
# # print(reviews_1)
# for review in reviews_1:
#     title = 'Doctors & Dentists'
#     paragraphs = review.find_all('p')
    
#     # Loop setiap p
#     for paragraph in paragraphs:
#         # Ambil nama dari elemen <a> pertama jika ada
#         name = ''
#         if paragraph.find('a'):
#             name = paragraph.find('a').get_text().strip()
#             url = paragraph.find('a')['href']
#         else:
#             # Jika tidak ada <a>, pastikan konten pertama adalah string sebelum mengakses strip()
#             first_content = paragraph.contents[0]
#             if isinstance(first_content, str):
#                 name = first_content.strip()
#             url = ''
        
#         address = ''
#         contact = ''
        
        
#         # Loop melalui isi paragraf untuk mendapatkan alamat dan kontak
#         for content in paragraph.contents:
#             if isinstance(content, str):
#                 text = content.strip()
#                 if any(char.isdigit() for char in text) and '-' in text:
#                     contact = text
#                 elif not contact and text and 'http' not in text:
#                     address += text + ' '


#         save_data = {
#             'Title': title,
#             'Name': name,
#             'Address': address.strip(),
#             'Contact': contact,
#             'Url': url
#         }
#         data.append(save_data)

#         # Cetak data sebagai debug
#         print(f"Name: {save_data['Name']}")
#         print(f"Address: {save_data['Address']}")
#         print(f"URL: {save_data['Url']}")
#         print()

# # print(data)

# # Buat DataFrame dari list data
# df = pd.DataFrame(data)

# # Tentukan nama folder dan buat jika belum ada
# folder_name = 'Rockland County'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Simpan DataFrame ke file CSV dengan nama berdasarkan title
# file_name = os.path.join(folder_name, f"{title}.csv")
# df.to_csv(file_name, index=False)

# print(f"Data berhasil disimpan ke '{file_name}'")

# Mengambil semua elemen div dengan class 'et_pb_toggle_content clearfix'
reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})

for review in reviews_1:
    # Mengambil elemen <p> di dalam review, jika ada
    paragraph_1 = review.find('p')

    # Memastikan bahwa <p> ditemukan sebelum mencari <a>
    if paragraph_1:
        # Mengambil elemen <a> di dalam <p>, jika ada
        a_tag = paragraph_1.find('a')

        # Memastikan bahwa <a> ditemukan sebelum mencoba mengambil URL dan teks
        if a_tag:
            url = a_tag.get('href')
            text = a_tag.text
            print("URL:", url)
            print("Text:", text)



reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})
for review in reviews_1:
    # Temukan semua elemen <p>
    title_1 = review.find_all('h3')
    # print(title_1)
    
    title = 'BABYSITTING, NANNIES & PET CARE'
    # Loop melalui setiap <p>
    for paragraph_1 in title_1:

        # title_up =  paragraph_1.text.strip()
        p_sibling = paragraph_1.find_next_sibling('p')        
        text_with_commas = ', '.join(p_sibling.stripped_strings)
        
        # print(paragraph_1.text.strip())
        # print(text_with_commas)

        save_data = {
            'Title' : title,
            'Name' : paragraph_1.text.strip(),
            'Address': text_with_commas
        }
        
        data.append(save_data)
        print('Saving', save_data['Name'], save_data['Name'], save_data['Address'])

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for item in data:
                writer.writerow(item)













# # Buat DataFrame dari list data
# df = pd.DataFrame(data)

# # Tentukan nama folder dan buat jika belum ada
# folder_name = 'CSV'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Simpan DataFrame ke file CSV dengan nama berdasarkan title
# file_name = os.path.join(folder_name, f"{title}.csv")
# df.to_csv(file_name, index=False)

# print(f"Data berhasil disimpan ke '{file_name}'")




# reviews_2 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})
# for review in reviews_1:
#     # Temukan semua elemen <p>
#     title_2 = review.find_all('h2')
#     # print(title_1)

#     # Loop melalui setiap <p>
#     for paragraph_2 in title_2:
#         # Inisialisasi variabel
#         # title = 'Dentists'
#         # name = ''
#         # address = ''
#         # contact = ''
#         # url = ''
        
#         print(paragraph_2.text.strip())




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
