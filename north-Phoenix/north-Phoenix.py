import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    'cookie':'_gid=GA1.2.55647415.1732027868; _fbp=fb.1.1732027898030.851295606654550932; _ga_96MDJBENSY=GS1.1.1732027840.1.1.1732029313.0.0.0; _ga=GA1.1.1322566091.1732027840; _ga_3XSHXF50QN=GS1.2.1732027916.1.1.1732029317.0.0.0'
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://northphoenixmomsnetwork.com/resources/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://northphoenixmomsnetwork.com/resources/home-services/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

title_name = 'Home Services'

reviews_1 = soup.find_all('div', {'class': 'entry-content'})

for page_ in reviews_1:
    paragraphs_1 = page_.find_all('p')
    # print(paragraphs_1)

    for p in paragraphs_1:
        a_tag = p.find('a')
        if a_tag:
            name = a_tag.text
            url = a_tag['href']
            
            # address = p.get_text(strip=True).replace(name, '').strip()
            address = ', '.join(p.stripped_strings)
            # address = p.get_text(strip=True).replace(name, '').strip()
            # address = address if address else 'none'
            address = address.replace(name, '').strip()
            address = address.lstrip(', ') 

            results.append({
                'County':'North Phoenix',
                'Title' : title_name,
                'Name': name,
                'Address': address.replace('Click for details!','').replace('Click for reservations!',''),
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
