import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    'cookie':'_fbp=fb.1.1732807659922.616212447387960585; __gads=ID=b1eea2652e44ef80:T=1732807657:RT=1732837025:S=ALNI_MYlkdctaMg9t0iO6yJ0s5LyhcRS2Q; __gpi=UID=00000fa1cc4b19b7:T=1732807657:RT=1732837025:S=ALNI_MZ0acyeJcCaT6UzA4H_waXWrmw0iw; __eoi=ID=4633d3281cb05a2a:T=1732807657:RT=1732837025:S=AA-AfjYQHzPvZMAiuMgc9jtEu58T'
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://thewesthollywoodmoms.com/resources/',
    'sec-ch-ua': 'Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://thewesthollywoodmoms.com/resources/childrens-activities/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

title_name = 'New Moms'

# Mencari semua <div> dengan kelas tertentu
divs = soup.find_all('div', class_='et_pb_toggle_content clearfix')

# Menyimpan data dalam bentuk list of dictionaries
data = []

for div in divs:
    current_entry = {}
    for p in div.find_all('p'):
        text = p.get_text(strip=True)
        link = p.find('a')
        href = link['href'] if link else None

        if href:
            # Jika sudah ada entry sebelumnya, simpan ke data
            if current_entry:
                data.append(current_entry)
                current_entry = {}

            current_entry['Name'] = text
            current_entry['Url'] = href

        elif text and text != '\xa0':  # Abaikan elemen kosong
            if 'Address' not in current_entry:
                current_entry['Address'] = text
            else:
                current_entry['Address'] += f", {text}"

    # Tambahkan entry terakhir jika ada
    if current_entry:
        data.append(current_entry)

# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})

# div = soup.find('div', class_='et_pb_toggle_content clearfix')

# # Menyimpan data dalam bentuk list of dictionaries
# data = []
# current_entry = {}

# for p in div.find_all('p'):
#     text = p.get_text(strip=True)
#     link = p.find('a')
#     href = link['href'] if link else None

#     if href:
#         # Jika sudah ada entry sebelumnya, simpan ke data
#         if current_entry:
#             data.append(current_entry)
#             current_entry = {}

#         current_entry['Name'] = text
#         current_entry['Url'] = href

#     elif text and text != '\xa0':  # Abaikan elemen kosong
#         if 'Address' not in current_entry:
#             current_entry['Address'] = text
#         else:
#             current_entry['Address'] += f", {text}"

# # Tambahkan entry terakhir jika ada
# if current_entry:
#     data.append(current_entry)


for result in data:
    print(f"Name = {result.get('Name', 'N/A')}")
    print(f"Address = {result.get('Address', 'N/A')}")
    print(f"Url = {result.get('Url', 'N/A')}")
    print()

# print(data)



# results = []  # Pastikan results didefinisikan sebelumnya

# for page in reviews_1:
#     # Temukan semua elemen <p> dalam <div>
#     paragraphs = page.find_all('p')

#     # Proses setiap blok alamat
#     data = []
#     current_entry = {}

#     for p in paragraphs:
#         # Ambil teks dan tautan (jika ada)
#         text = p.get_text(strip=True)
#         link = p.find('a')
#         href = link['href'] if link else None

#         # Jika <a> ditemukan, itu adalah nama dan URL
#         if href:
#             # Simpan entry sebelumnya jika ada
#             if current_entry:
#                 data.append(current_entry)
#                 current_entry = {}

#             current_entry['Name'] = text
#             current_entry['Url'] = href

#         elif text and text != '\xa0':  # Abaikan elemen kosong atau hanya spasi
#             if 'Address' not in current_entry:
#                 current_entry['Address'] = text
#             else:
#                 current_entry['Address'] += f", {text}"

#     # Tambahkan entry terakhir jika ada
#     if current_entry:
#         results.append(current_entry)

# # Cetak hasil
# for result in results:
#     print(f"Name = {result.get('Name', 'N/A')}")
#     print(f"Address = {result.get('Address', 'N/A')}")
#     print(f"Url = {result.get('Url', 'N/A')}")
#     print()

    # filename = f"{title_name}.csv"

    # with open(filename, mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','url'])
    #     writer.writeheader()  
    #     writer.writerows(results)  

    # print(f"Data telah disimpan ke dalam file '{filename}'")



# for page_ in reviews_1:
#     paragraphs_1 = page_.find_all('p')
#     # print(paragraphs_1)

#     for p in paragraphs_1:
#         name_element = p.find('a')
#         name = name_element.text.strip() if name_element else ''
#         a_tag = p.find('a')
#         if a_tag:
#             # name = a_tag.text
#             url = a_tag['href']
            
#             # # address = p.get_text(strip=True).replace(name, '').strip()
#             # address = ', '.join(p.stripped_strings)
#             # address = p.get_text(strip=True).replace(name, '').replace(url, '').strip()
#             # # address = address if address else 'none'
#             # # address = address.replace(name, '').strip()
#             # address = address.lstrip(', ') 

#             address = ', '.join(p.stripped_strings)

#             # Hapus 'name' dan 'url' dari teks
#             address = address.replace(name, '').replace(url, '').strip()

#             # Atur default jika address kosong
#             address = address if address else 'none'

#             # Hapus koma di awal teks, jika ada
#             address = address.lstrip(', ')

#             results.append({
#                 'County':'Santa Barbara',
#                 'Title' : title_name,
#                 'Name': name,
#                 'Address': address,
#                 'Contact': '',
#                 'Email':'',
#                 'url': url
#             })


# for result in results:
#     print(f"County = {result['County']}")
#     print(f"Title = {result['Title']}")
#     print(f"Name = {result['Name']}")
#     print(f"Address = {result['Address']}")
#     print(f"Contact = {result['Contact']}")
#     print(f"Email = {result['Email']}")
#     print(f"url = {result['url']}")
#     print() 
               
# filename = f"{title_name}.csv"

# with open(filename, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','url'])
#     writer.writeheader()  
#     writer.writerows(results)  

# print(f"Data telah disimpan ke dalam file '{filename}'")

