import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    'cookie':'_ga=GA1.1.1749511176.1732328238; _fbp=fb.1.1732328238834.715974469757463851; __gads=ID=48ce52c8b2fbc0a5:T=1732328239:RT=1732459775:S=ALNI_Mb4SC6F--_kLZKBcx3lMVWWr79nuA; __gpi=UID=00000f728fee63a5:T=1732328239:RT=1732459775:S=ALNI_MbC78cWyuN7UFCZgf46fHybGkHgHw; __eoi=ID=b81706f17b9e0d6e:T=1732328239:RT=1732459775:S=AA-Afjbb0XZ0GgyLeeLYfXNhA9dc; cf_clearance=w8nhWCMjG3ZaNal4BuJibD2yxlVfr8EWyOQlUWn1XqQ-1732460046-1.2.1.1-gB2s_xUsHyvpT7e4BnGdvhmQ1lNDO33gSJFFTxVcqTnBpmzLxNDv.aq_gsdEXNR5_lu64SAboJFjXOi8MYv7ComxUr5eV6cP7R9i1RbWBYbLe2klY9BK6Pw6gTO.DYMnhSIXL2Spe53xAKlC8lMQ8rlxUlUZ4aD8bOaHUsaJGbHoBJn_oRnz1k1z._EbI2J29hQYItc78P374dF2c8zklTCPpkr1wElIVHpHikQdRnpGvv_e9TY1M.ZVV4AkeRXJMuROMH_.K.V32vrnVM_cihx62_YiLN_NB1_hful63Is_JwwdQyuaW8pzFtofAlOGECYo8a8KHDuFkGTuv_0kYUN..Ywr_i48cx_BdJLkXja00AopelVfbL5q95c6bAs28f_3.ZA7tQV5AnyXyrs9W10pbxVak_hIXgENnxFIDRk; _ga_Z5XB5W5D00=GS1.1.1732456156.3.1.1732460060.0.0.0'
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://beachcitiesmoms.com/resources/',
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

response = requests.get('https://beachcitiesmoms.com/resources/family-dining/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

title_name = 'Family Dining'

reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})

for page_ in reviews_1:
    paragraphs_1 = page_.find_all('p')
    # print(paragraphs_1)

    for p in paragraphs_1:
        name_element = p.find('strong')
        name = name_element.text.strip() if name_element else ''
        a_tag = p.find('a')
        if a_tag:
            # name = a_tag.text
            url = a_tag['href']
            
            # address = p.get_text(strip=True).replace(name, '').strip()
            address = ', '.join(p.stripped_strings)
            address = p.get_text(strip=True).replace(name, '').replace(url, '').strip()
            address = address if address else 'none'
            # address = address.replace(name, '').strip()
            address = address.lstrip(', ') 

            results.append({
                'County':'Beach Cities',
                'Title' : title_name,
                'Name': name,
                'Address': address,
                'Contact': '',
                'Email':'',
                'url': url
            })


for result in results:
    print(f"County = {result['County']}")
    print(f"Title = {result['Title']}")
    print(f"Name = {result['Name']}")
    print(f"Address = {result['Address']}")
    print(f"Contact = {result['Contact']}")
    print(f"Email = {result['Email']}")
    print(f"url = {result['url']}")
    print() 
               
filename = f"{title_name}.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','url'])
    writer.writeheader()  
    writer.writerows(results)  

print(f"Data telah disimpan ke dalam file '{filename}'")

