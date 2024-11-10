import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    '_fbp': 'fb.1.1727272184560.436269777395599014',
    'pmc_atlasmg_id': '6386ac4a-a262-4608-9ae6-29a626576ef4',
    '__td_signed': 'true',
    '__td_blockEvents': 'false',
    'permutive-id': '39c0a8c6-a3af-45d4-a59c-c2e27e0f6f3f',
    '_gid': 'GA1.2.663785626.1727272196',
    'cto_bundle': 'w1zgyl9qZ3RvMXZEcGFzUkxyVld3TG5DbWRhc3h3TXE5QURvaEhMVUpyNUFWMVYlMkJRTTliWFFqQ3N4d3ZkWlhnODI5S0tsZUVZdk5ianoydzhmZ2kwTDFzSkpPWGJXd0g2azV5cXZ1d2tic0ZlZ2tsY0VTdSUyRmh4ZGZKcFhMVkFJVHN5SlRFYTdVa2pFc2FYJTJCJTJGV3JqRGtSUHlRR21Xbm1wdUVJcXpJWG80RXpodjd4Q1QzcUhwMmhPQllUQ2tyQ1lPaHVSbDY5YVlxQkI1bm9RZ0M2OXdmeGZPVnlBdDh0TlBvV252eGV0R01oSUFYUzVTcW9icDE3RDRTc1JSS1JNbEdKbHN5JTJCelZTSWJ6NkZBJTJCbnN5dFE1UlYxQSUzRCUzRA',
    '_lr_env_src_ats': 'false',
    '_lr_geo_location': 'ID',
    'MCPopupClosed': 'yes',
    '_cc_id': 'a3b14cffeb8408c4ae5b7a6c5e63dfb0',
    'panoramaId': '7af3c29c7343d92fb110e7ffab88a9fb927a716dcbe4da8427adccf9942e1ac6',
    'panoramaIdType': 'panoDevice',
    '_au_1d': 'AU1D-0100-001727272209-HTUZS66X-90GX',
    'cnx_userId': 'd8c3b48797c34355b9714708a829e3f9',
    'panoramaId_expiry': '1727358619565',
    '_lr_retry_request': 'true',
    '_ga_FVWZ0RM4DH': 'GS1.1.1727306538.4.1.1727308913.60.0.0',
    '_ga_5ED67KSQBC': 'GS1.1.1727305979.4.1.1727309055.0.0.0',
    '_td': '2a6790df-39c0-42d9-8016-3cfdb1192196',
    '_ga_CGRZHQ8KQD': 'GS1.1.1727305981.4.1.1727309060.60.0.0',
    'FCNEC': '%5B%5B%22AKsRol9WSlPW_TYvv8nda-L7ybc6xZ9VE9lonb09ZmpfKaycOj5DwqB_AEWNq_PniHhGEw3OPrbPgz5i2a4nHFbK0AatduHHVFyQV9EzDSyGvYZtuezj5VUqclCFTGHkOsVOUQm3dIIFP0KXIFIbhdWhYjk9dqGqiw%3D%3D%22%5D%5D',
    '__gads': 'ID=8d6f27282db3f50a:T=1727272191:RT=1727309284:S=ALNI_MYi7pEkmbroxZltFLrAGZ68v6cLfw',
    '__gpi': 'UID=00000f1d8dcf0af8:T=1727272191:RT=1727309284:S=ALNI_MaS7c4i-q7xJOkVTbEANAy3uou1xA',
    '__eoi': 'ID=fb7eef1506f18bb2:T=1727272191:RT=1727309284:S=AA-AfjZd_iRTnHVNAsLekeeHMEi2',
    '_ga': 'GA1.2.2085893758.1727272183',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_fbp=fb.1.1727272184560.436269777395599014; pmc_atlasmg_id=6386ac4a-a262-4608-9ae6-29a626576ef4; __td_signed=true; __td_blockEvents=false; permutive-id=39c0a8c6-a3af-45d4-a59c-c2e27e0f6f3f; _gid=GA1.2.663785626.1727272196; cto_bundle=w1zgyl9qZ3RvMXZEcGFzUkxyVld3TG5DbWRhc3h3TXE5QURvaEhMVUpyNUFWMVYlMkJRTTliWFFqQ3N4d3ZkWlhnODI5S0tsZUVZdk5ianoydzhmZ2kwTDFzSkpPWGJXd0g2azV5cXZ1d2tic0ZlZ2tsY0VTdSUyRmh4ZGZKcFhMVkFJVHN5SlRFYTdVa2pFc2FYJTJCJTJGV3JqRGtSUHlRR21Xbm1wdUVJcXpJWG80RXpodjd4Q1QzcUhwMmhPQllUQ2tyQ1lPaHVSbDY5YVlxQkI1bm9RZ0M2OXdmeGZPVnlBdDh0TlBvV252eGV0R01oSUFYUzVTcW9icDE3RDRTc1JSS1JNbEdKbHN5JTJCelZTSWJ6NkZBJTJCbnN5dFE1UlYxQSUzRCUzRA; _lr_env_src_ats=false; _lr_geo_location=ID; MCPopupClosed=yes; _cc_id=a3b14cffeb8408c4ae5b7a6c5e63dfb0; panoramaId=7af3c29c7343d92fb110e7ffab88a9fb927a716dcbe4da8427adccf9942e1ac6; panoramaIdType=panoDevice; _au_1d=AU1D-0100-001727272209-HTUZS66X-90GX; cnx_userId=d8c3b48797c34355b9714708a829e3f9; panoramaId_expiry=1727358619565; _lr_retry_request=true; _ga_FVWZ0RM4DH=GS1.1.1727306538.4.1.1727308913.60.0.0; _ga_5ED67KSQBC=GS1.1.1727305979.4.1.1727309055.0.0.0; _td=2a6790df-39c0-42d9-8016-3cfdb1192196; _ga_CGRZHQ8KQD=GS1.1.1727305981.4.1.1727309060.60.0.0; FCNEC=%5B%5B%22AKsRol9WSlPW_TYvv8nda-L7ybc6xZ9VE9lonb09ZmpfKaycOj5DwqB_AEWNq_PniHhGEw3OPrbPgz5i2a4nHFbK0AatduHHVFyQV9EzDSyGvYZtuezj5VUqclCFTGHkOsVOUQm3dIIFP0KXIFIbhdWhYjk9dqGqiw%3D%3D%22%5D%5D; __gads=ID=8d6f27282db3f50a:T=1727272191:RT=1727309284:S=ALNI_MYi7pEkmbroxZltFLrAGZ68v6cLfw; __gpi=UID=00000f1d8dcf0af8:T=1727272191:RT=1727309284:S=ALNI_MaS7c4i-q7xJOkVTbEANAy3uou1xA; __eoi=ID=fb7eef1506f18bb2:T=1727272191:RT=1727309284:S=AA-AfjZd_iRTnHVNAsLekeeHMEi2; _ga=GA1.2.2085893758.1727272183',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://soundshoremoms.com/resources/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://soundshoremoms.com/get-lost-in-fun-the-best-corn-mazes-in-and-around-westchester-ny/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

# title_name = 'Learning Support Tutoring Services'


# divs = soup.find_all('div', class_='et_pb_text_inner')
# for div in divs:
#     # Ambil title dari <a> dalam <div>
#     a_tag = div.find('a')
#     title = a_tag.get_text(strip=True) if a_tag else None
#     url = a_tag['href'] if a_tag else None

#     # Ambil informasi lainnya dari <p> dalam <div>
#     paragraphs = div.find_all('p')
#     address = []
#     phone = None

#     for p in paragraphs:
#         text = p.get_text(strip=True)
        
#         # Deteksi phone number
#         if '(' in text and ')' in text and '-' in text:
#             phone = text
#         # Anggap teks lain adalah bagian dari alamat
#         elif text:
#             address.append(text)

#     # Gabungkan address menjadi satu string dengan koma sebagai pemisah
#     address = ', '.join(address) if address else None

#     results.append({
#         'Title' : title_name,
#         'Name': title,
#         'Address': address,
#         'Contact': phone,
#         'Email':'',
#         'url': url
#     })


# Print hasilnya


# # Ambil semua elemen <div> dengan class 'et_pb_text_inner'
# divs = soup.reviews_1('div', class_='et_pb_text_inner')
# for div in divs:
#     # Ambil title dari <a> dalam <div>
#     a_tag = div.find('a')
#     title = a_tag.get_text(strip=True) if a_tag else None
#     url = a_tag['href'] if a_tag else None

#     # Ambil informasi lainnya dari <p> dalam <div>
#     paragraphs = div.find_all('p')
#     phone = None
#     email = None
#     age_group = None
#     location = None

#     for p in paragraphs:
#         text = p.get_text(strip=True)
        
#         # Deteksi pola untuk phone number
#         if '(' in text and ')' in text and '-' in text:
#             phone = text
#         # Deteksi pola untuk email
#         elif '@' in text:
#             email = text
#         # Deteksi pola untuk age group
#         elif text.startswith("Ages:"):
#             age_group = text.replace("Ages:", "").strip()
#         # Deteksi pola untuk lokasi
#         elif text.startswith("Location:"):
#             location = text.replace("Location:", "").strip()

#     # Simpan hasil ke dalam dictionary
#     results.append({
#         'title': title,
#         'url': url,
#         'phone': phone,
#         'email': email,
#         'age_group': age_group,
#         'location': location
#     })

# # Print hasilnya
# for result in results:
#     print(f"title = {result['title']}")
#     print(f"url = {result['url']}")
#     print(f"phone = {result['phone']}")
#     print(f"email = {result['email']}")
#     print(f"age_group = {result['age_group']}")
#     print(f"location = {result['location']}")
#     print()

# for page in reviews_1:
#     paragraphs_1 = page.find_all('et_pb_text_inner')
#     print(paragraphs_1)
    
    # for p in paragraphs_1:
    #     a_tag = p.find('a')
    #     if a_tag:
    #         name = a_tag.text
    #         url = a_tag['href']
    #         # Ambil alamat jika ada
    #         # address = p.get_text(strip=True).replace(name, '').strip()
    #         address = ', '.join(p.stripped_strings)

    #         # address = p.get_text(strip=True).replace(name, '').strip()
    #         # address = address if address else 'none'
    #         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
    #         address = address.lstrip(', ')  # Menghapus koma pertama jika ada

    #         results.append({
    #             'Title' : '',
    #             'Name': name,
    #             'address': address,
    #             'Contact':'',
    #             'url': url,
    #             'Email':''
    #         })



# reviews_1 = soup.find_all('div', {'class': 'et_pb_text_inner'})
# # print(reviews_1)
# for page in reviews_1: 

#     paragraphs = page.find_all('p')

# for p in paragraphs:
#     # Ambil title dari <strong> atau <a> dalam <p>
#     strong_tag = p.find('strong')
#     a_tag = p.find('a')
#     title = strong_tag.get_text(strip=True) if strong_tag else (a_tag.get_text(strip=True) if a_tag else None)
    
#     # Ambil alamat (address) dengan menggunakan <br> setelah title, jika ada strong_tag
#     address = ""
#     if strong_tag:
#         for sibling in strong_tag.next_siblings:
#             if sibling.name == 'br':
#                 # Setelah <br>, ambil teks berikutnya sebagai address
#                 address = sibling.next.strip() if sibling.next else ""
#                 break

#     # Ambil deskripsi dari teks setelah alamat
#     description = ""
#     if address and ',' in address:
#         address_parts = address.split(',')
#         address = address_parts[0].strip()  # Bagian pertama sebagai address
#         description = ', '.join(address_parts[1:]).strip()  # Sisanya sebagai deskripsi

#     # Ambil URL dari elemen <a> jika ada
#     url = a_tag['href'] if a_tag else None

#     # Simpan hasil ke dalam dictionary
#     results.append({
#         'title': title,
#         'address': address,
#         'description': description,
#         'url': url
#     })



# title_name = 'Guides - Pumpkin Patches in Westchester, NY'

# reviews_1 = soup.find_all('div', {'class': 'et_pb_text_inner'})
# # print(reviews_1)
# for page in reviews_1: 

#     paragraphs = page.find_all('p')
#     for p in paragraphs:
#         # Ambil title dari <strong> dalam <p>
#         strong_tag = p.find('strong')
#         title = strong_tag.get_text(strip=True) if strong_tag else None

#         # Cari lokasi dengan elemen <em> yang berisi teks 'Location:'
#         location_tag = p.find('em', string='Location:')
#         location = location_tag.next_sibling.strip() if location_tag and location_tag.next_sibling else None

#         # Cari deskripsi dengan elemen <em> yang berisi teks 'Description:'
#         # description_tag = p.find('em', text='Description:')
#         # description = description_tag.next_sibling.strip() if description_tag and description_tag.next_sibling else None

#         # Ambil URL dari elemen <a> jika ada
#         a_tag = p.find('a')
#         url = a_tag['href'] if a_tag else None

#         results.append({
#             'Title' : title_name,
#             'Name': title,
#             'Address': location,
#             'Contact': '',
#             'Email':'',
#             'url': url
#         })




# for page in reviews_1:

#     paragraphs = page.find_all('p')
#     for p in paragraphs:
#         strong_tag = p.find('strong')
#         title = None
        
#         # Cek apakah ada <a> di dalam <strong>, jika ada ambil teks dari <a>
#         if strong_tag:
#             a_tag_in_strong = strong_tag.find('a')
#             title = a_tag_in_strong.text.strip() if a_tag_in_strong else strong_tag.text.strip()

#         # Lanjutkan ke elemen berikutnya jika tidak ada title
#         if not title:
#             continue

#         # Mengumpulkan teks untuk address, kecuali title
#         address_parts = [text.strip() for text in p.stripped_strings if text != title]
#         address = ', '.join(address_parts)

#         # Mengambil URL dari elemen <a> di luar <strong>, jika ada
#         a_tag = p.find('a')
#         url = a_tag['href'] if a_tag else None

#         # Tambahkan data ke results
#         results.append({
#             'name': title,
#             'address': address,
#             'url': url,
#             'Email' : ''
#         })


# for page in reviews_1:

#     for p in paragraphs:
#         if a_tag:
#             name = a_tag.text
#             url = a_tag['href']
#             # Ambil alamat jika ada
#             # address = p.get_text(strip=True).replace(name, '').strip()
#             address = ', '.join(p.stripped_strings)

#             # address = p.get_text(strip=True).replace(name, '').strip()
#             # address = address if address else 'none'
#             address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#             address = address.lstrip(', ')  # Menghapus koma pertama jika ada


#         results.append({
#             'Title' : title_name,
#             'Name': name,
#             'Address': address,
#             'Contact': '',
#             'Email':'',
#             'url': url
#         })

# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})

# for page in reviews_1:
#     # Temukan semua elemen <h3> di dalam HTML
#     # Loop untuk setiap elemen <h3>
#     headings = page.find_all('h4')
#     for h in headings:
#         # Ambil title dari <strong> dalam <h4>
#         strong_tag = h.find('strong')
#         title = strong_tag.get_text(strip=True) if strong_tag else None

#         # Ambil URL dari <a> dalam <h4>
#         a_tag = h.find('a')
#         url = a_tag['href'] if a_tag else None

#         # Ambil address dari semua teks lain dalam <h4> (selain title dan URL)
#         address_parts = [text.strip() for text in h.stripped_strings if text != title and (not a_tag or text != a_tag.get_text(strip=True))]
#         address = ', '.join(address_parts)

#         # Tambahkan hasil ke list
#         results.append({
#             'name': title,
#             'url': url,
#             'address': address.strip(),
#             'Email':''
#         })

# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})

# for page in reviews_1:
#     # Temukan semua elemen <h3> di dalam HTML
#     # Loop untuk setiap elemen <h3>
#     titles = page.find_all('h3')
#     for title in titles:
#         # Ambil teks dari elemen <h3> sebagai title
#         title_text = title.text.strip()
#         address = ""
#         url = None

#         # Loop setiap sibling setelah <h3>
#         for sibling in title.find_next_siblings():
#             # Berhenti jika sibling berikutnya adalah <h3> lainnya
#             if sibling.name == 'h3':
#                 break
            
#             # Jika sibling adalah <p> dengan teks, tambahkan ke address
#             if sibling.name == 'p' and sibling.find('a') is None:
#                 address += ', '.join(sibling.stripped_strings) + " "
            
#             # Jika sibling adalah <p> dengan elemen <a>, ambil url
#             if sibling.find('a'):
#                 a_tag = sibling.find('a')
#                 url = a_tag['href']

#         # Membuat dictionary untuk setiap entry
#         # entry = {
#         #     'title': title_text,
#         #     'address': address.strip(),  # Hapus spasi ekstra di akhir
#         #     'url': url
#         # }
#         # results.append(entry)

#         results.append({
#             'name': title_text,
#             'url': url,
#             'address': address.strip(),
#             'Email':''
#         })

# # Print hasil
# for result in results:
#     print(result)





title_name = 'Guides - Get Lost in Fun: The Best Corn Mazes in and Around Westchester, NY'

reviews_1 = soup.find_all('div', {'class': 'et_pb_text_inner'})

for page_ in reviews_1:
    paragraphs_1 = page_.find_all('p')
    # print(paragraphs_1)

    for p in paragraphs_1:
        a_tag = p.find('a')
        if a_tag:
            name = a_tag.text
            url = a_tag['href']
            # Ambil alamat jika ada
            # address = p.get_text(strip=True).replace(name, '').strip()
            address = ', '.join(p.stripped_strings)

            # address = p.get_text(strip=True).replace(name, '').strip()
            # address = address if address else 'none'
            address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
            address = address.lstrip(', ')  # Menghapus koma pertama jika ada

            results.append({
                'Title' : title_name,
                'Name': name,
                'Address': address.replace('Click for details!','').replace('Click for reservations!',''),
                'Contact': '',
                'Email':'',
                'url': url
            })



# benar 1

# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[0]
# paragraphs_1 = reviews_1.find_all('p')
# # print(paragraphs)



# for p in paragraphs_1:
#     a_tag = p.find('a')
#     if a_tag:
#         name = a_tag.text
#         url = a_tag['href']
#         # Ambil alamat jika ada
#         # address = p.get_text(strip=True).replace(name, '').strip()
#         address = ', '.join(p.stripped_strings)

#         # address = p.get_text(strip=True).replace(name, '').strip()
#         # address = address if address else 'none'
#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address,
#             'Email':''
#         })



# Temukan semua elemen <p> di dalam div
# reviews_2 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[1]
# title_2 = reviews_2.find_all('h3')

# for paragraph_1 in title_2:
#     # Mencari sibling <p> dari <h3>
#     p_sibling = paragraph_1.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling:
#         # Menampilkan teks dari elemen <h3>
#         name = paragraph_1.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address = ', '.join(p_sibling.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag = p_sibling.find('a')
#         url = a_tag['href'] if a_tag else None

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address,
#             'Email':''
#         })

# reviews_3 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[2]
# title_3 = reviews_3.find_all('h3')

# for paragraph_3 in title_3:
#     # Mencari sibling <p> dari <h3>
#     p_sibling_ = paragraph_3.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling_:
#         # Menampilkan teks dari elemen <h3>
#         name_ = paragraph_3.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address_ = ', '.join(p_sibling_.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag_ = p_sibling_.find('a')
#         url_ = a_tag_['href'] if a_tag_ else None

#         results.append({
#             'name': name_,
#             'url': url_,
#             'address': address_,
#             'Email':''
#         })

# reviews_4 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[3]
# title_4 = reviews_4.find_all('h3')

# for paragraph_4 in title_4:
#     # Mencari sibling <p> dari <h3>
#     p_sibling_4 = paragraph_4.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling_4:
#         # Menampilkan teks dari elemen <h3>
#         name_4 = paragraph_4.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address_4 = ', '.join(p_sibling_4.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag_4 = p_sibling_4.find('a')
#         url_4 = a_tag_['href'] if a_tag_4 else None

#         results.append({
#             'name': name_4,
#             'url': url_4,
#             'address': address_4,
#             'Email':''
#         })


# # Temukan semua elemen <h3> di dalam HTML
# titles = soup.find_all('h3')

# # Loop setiap elemen <h3>

# for title in titles:
#     # Ambil teks dari elemen <h3>
#     name = title.text.strip()
#     # print(f"Title: {title_text}")
    
#     # Ambil semua sibling setelah <h3> hingga <h3> berikutnya
#     for sibling in title.find_next_siblings():
#         # Berhenti jika sibling berikutnya adalah <h3> lainnya
#         if sibling.name == 'h3':
#             break
#         # Jika sibling adalah <p>, ambil teksnya
#         if sibling.name == 'p':
#             address = sibling.text.strip()
#             print(name)
#             print(address)
    


# titles = soup.find_all('h3')

# # Loop untuk setiap elemen <h3> sebagai title
# for title in titles:
#     # Ambil teks dari elemen <h3> sebagai name
#     name = title.text.strip()
#     addresses = []  # List untuk menampung semua alamat terkait

#     # Loop setiap sibling setelah <h3>
#     for sibling in title.find_next_siblings():
#         # Berhenti jika sibling berikutnya adalah <h3> lainnya
#         if sibling.name == 'h3':
#             break

#         # Jika sibling adalah <p>, ambil teksnya dan tambahkan ke list addresses
#         if sibling.name == 'p':
#             address = sibling.text.strip()
#             addresses.append(address)

#     # Buat dictionary untuk tiap entry dan tambahkan ke results
#     if addresses:
#         save_data = {
#             'Name': name,
#             'Address': addresses
#         }
#         results.append(save_data)
#         print('Saving', save_data['Name'], save_data['Address'])

# reviews_2 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[3]
# paragraphs_2 = reviews_2.find_all('p')
# # print(paragraphs)



# for p in paragraphs_2:
#     a_tag = p.find('a')
#     if a_tag:
#         name = a_tag.text
#         url = a_tag['href']
#         # Ambil alamat jika ada
#         # address = p.get_text(strip=True).replace(name, '').strip()
#         address = ', '.join(p.stripped_strings)

#         # address = p.get_text(strip=True).replace(name, '').strip()
#         # address = address if address else 'none'
#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address,
#             'Email':''
#         })


# reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[0]

# paragraphs_1 = reviews_1.find_all('p')
# for p in paragraphs_1:
#     strong_tag = p.find('strong')
#     name = strong_tag.text.strip() if strong_tag else None  # Mendapatkan teks dari <strong> jika ada
#     a_tag = p.find('a')
    
#     if name:  # Pastikan name tersedia
#         url = a_tag['href'] if a_tag else None  # Ambil URL jika <a> ada, jika tidak biarkan None

#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         # Menghapus bagian 'Click here' dan 'for more information.' jika ada
#         address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
#         address = ', '.join(p.stripped_strings)
        
#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada
#         results.append({
#             'name': name,
#             'url': url if url else '',  # Kosongkan URL jika tidak ada
#             'address': address.replace(url,''),
#             'Email': ''
#         })

# reviews_2 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[1]

# paragraphs_2 = reviews_2.find_all('p')
# for p in paragraphs_2:
#     strong_tag = p.find('strong')
#     name = strong_tag.text.strip() if strong_tag else None  # Mendapatkan teks dari <strong> jika ada
#     a_tag = p.find('a')
    
#     if name:  # Pastikan name tersedia
#         url = a_tag['href'] if a_tag else None  # Ambil URL jika <a> ada, jika tidak biarkan None

#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         # Menghapus bagian 'Click here' dan 'for more information.' jika ada
#         address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
#         address = ', '.join(p.stripped_strings)
        
#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada
#         results.append({
#             'name': name,
#             'url': url if url else '',  # Kosongkan URL jika tidak ada
#             'address': address.replace(url,''),
#             'Email': ''
#         })

# reviews_4 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[5]

# paragraphs_4 = reviews_4.find_all('p')
# for p in paragraphs_4:
#     strong_tag = p.find('strong')
#     name = strong_tag.text.strip() if strong_tag else None  # Mendapatkan teks dari <strong> jika ada
#     a_tag = p.find('a')
    
#     if name:  # Pastikan name tersedia
#         url = a_tag['href'] if a_tag else None  # Ambil URL jika <a> ada, jika tidak biarkan None

#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         # Menghapus bagian 'Click here' dan 'for more information.' jika ada
#         address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
#         address = ', '.join(p.stripped_strings)

#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada
#         results.append({
#             'name': name,
#             'url': url if url else '',  # Kosongkan URL jika tidak ada
#             'address': address,
#             'Email': ''
#         })

# reviews_5 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[6]

# paragraphs_5 = reviews_5.find_all('p')
# for p in paragraphs_5:
#     strong_tag = p.find('strong')
#     name = strong_tag.text.strip() if strong_tag else None  # Mendapatkan teks dari <strong> jika ada
#     a_tag = p.find('a')
    
#     if name:  # Pastikan name tersedia
#         url = a_tag['href'] if a_tag else None  # Ambil URL jika <a> ada, jika tidak biarkan None

#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         # Menghapus bagian 'Click here' dan 'for more information.' jika ada
#         address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
#         address = ', '.join(p.stripped_strings)

#         address = address.replace(name, '').strip()  # Menghapus nama dan spasi tambahan
#         address = address.lstrip(', ')  # Menghapus koma pertama jika ada
#         results.append({
#             'name': name,
#             'url': url if url else '',  # Kosongkan URL jika tidak ada
#             'address': address,
#             'Email': ''
#         })



# # # Temukan semua elemen <p> di dalam div
# reviews_2 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[2]
# title_2 = reviews_2.find_all('h3')

# for paragraph_1 in title_2:
#     # Mencari sibling <p> dari <h3>
#     p_sibling = paragraph_1.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling:
#         # Menampilkan teks dari elemen <h3>
#         name = paragraph_1.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address = ', '.join(p_sibling.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag = p_sibling.find('a')
#         url = a_tag['href'] if a_tag else None

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address,
#             'Email':''
#         })

# reviews_3 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[2]
# title_3 = reviews_3.find_all('h3')

# for paragraph_3 in title_3:
#     # Mencari sibling <p> dari <h3>
#     p_sibling_3 = paragraph_3.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling_3:
#         # Menampilkan teks dari elemen <h3>
#         name = paragraph_3.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address = ', '.join(p_sibling_3.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag = p_sibling_3.find('a')
#         url = a_tag['href'] if a_tag else None

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address
#         })

# reviews_4 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[3]
# title_4 = reviews_4.find_all('h3')

# for paragraph_4 in title_4:
#     # Mencari sibling <p> dari <h3>
#     p_sibling_4 = paragraph_4.find_next_sibling('p')

#     # Menampilkan judul dan konten jika ditemukan
#     if p_sibling_4:
#         # Menampilkan teks dari elemen <h3>
#         name = paragraph_4.text.strip()
        
#         # Menampilkan teks dari <p> dan mengganti <br> dengan koma
#         address = ', '.join(p_sibling_4.stripped_strings)

#         # Mencari URL dalam <p> (jika ada)
#         a_tag = p_sibling_4.find('a')
#         url = a_tag['href'] if a_tag else None

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address
#         })

    # for p in p_sibling:
    #     strong_tag = p.find('strong')
    #     a_tag = p.find('a')
    #     em_tag = p.find('em')

    #     if strong_tag and a_tag:
    #         name = strong_tag.text.strip()
    #         url = a_tag['href']
    #         address = em_tag.text.strip() if em_tag else 'none'

    #         results.append({
    #             'name': name,
    #             'url': url,
    #             'address': address
    #         })




# # 3
# reviews_3 = soup.find_all('div', {'class': 'et_pb_text_inner'})[1]

# paragraphs_3 = reviews_3.find_all('p')

# for p in paragraphs_3:
#     strong_tag = p.find('strong')
#     print(strong_tag)
#     a_tag = p.find('a')
#     if strong_tag and a_tag:
#         name = strong_tag.text.strip()
#         url = a_tag['href']
#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         address = address.split('for more information.')[0].strip()
#         name = p.text.replace(url, '').replace('Click', '').replace('here', '').strip()

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address,
#             'Email':''
#         })



# reviews_3 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})[6]

# paragraphs_3 = reviews_3.find_all('p')
# for p in paragraphs_3:
#     strong_tag = p.find('strong')
#     name = strong_tag.text.strip() if strong_tag else None  # Mendapatkan teks dari <strong> jika ada
#     a_tag = p.find('a')
    
#     if name:  # Pastikan name tersedia
#         url = a_tag['href'] if a_tag else None  # Ambil URL jika <a> ada, jika tidak biarkan None

#         # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
#         # Menghapus bagian 'Click here' dan 'for more information.' jika ada
#         address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
#         address = ', '.join(p.stripped_strings)
        
#         results.append({
#             'name': name,
#             'url': url if url else '',  # Kosongkan URL jika tidak ada
#             'address': address,
#             'Email': ''
#         })


# reviews_4 = soup.find_all('div', {'class': 'et_pb_tab_content'})[3]
# paragraphs_4 = reviews_4.find_all('p')
# # print(paragraphs)


# for p in paragraphs_4:
#     a_tag = p.find('a')
#     if a_tag:
#         name = a_tag.text
#         url = a_tag['href']
#         # Ambil alamat jika ada
#         address = p.get_text(strip=True).replace(name, '').strip()
#         address = address if address else 'none'

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address
#         })

# reviews_5 = soup.find_all('div', {'class': 'et_pb_tab_content'})[4]
# paragraphs_5 = reviews_5.find_all('p')
# # print(paragraphs)

# # Inisialisasi daftar untuk menyimpan hasil


# for p in paragraphs_5:
#     a_tag = p.find('a')
#     if a_tag:
#         name = a_tag.text
#         url = a_tag['href']
#         # Ambil alamat jika ada
#         address = p.get_text(strip=True).replace(name, '').strip()
#         address = address if address else 'none'

#         results.append({
#             'name': name,
#             'url': url,
#             'address': address
#         })

# # Tampilkan hasil
for result in results:
    print(f"Title = {result['Title']}")
    print(f"Name = {result['Name']}")
    print(f"Address = {result['Address']}")
    print(f"Contact = {result['Contact']}")
    print(f"Email = {result['Email']}")
    print(f"url = {result['url']}")
    print()  # Untuk pemisah antar entri
               
filename = f"{title_name}.csv"

# Menulis data ke dalam file CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Title','Name','Address', 'Contact', 'Email','url'])
    writer.writeheader()  # Menulis header
    writer.writerows(results)  # Menulis data

print(f"Data telah disimpan ke dalam file '{filename}'")