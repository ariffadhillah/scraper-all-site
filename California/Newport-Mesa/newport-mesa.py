import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    'cookie':'_ga=GA1.1.823657898.1732619417; _fbp=fb.1.1732619418980.751282899794716027; __td_signed=true; __td_blockEvents=false; pmc_atlasmg_id=45489b5b-9c69-41e1-8a4d-0999c093752c; MCPopupClosed=yes; permutive-id=3cedbd0b-0059-4c7d-b42d-d18fef29581c; cf_clearance=v9NA7r3poV5X.dEhseYmhOps4vhiT6UDg9bkofM79Ag-1732719315-1.2.1.1-ASjAD8_u3Nxb4xqs9nbvD9K3I1KZ.nE7qniqJSbGjRR__Tmhkw5v._8P5LZzgx34WBMjwuIZ64Ta5tRmUQLqFoURfqBthS2WIFMadEP662c30DYImcDy6LnMOQvljYImyLP1x61jfM_HHalUc4_OLo0A7qMFH0ArmnP_RuKQBeJzFs8AafJeOtikhZwmMfZe5G2tTbWmRKwa.AUTIPO1HeQ2JmCnffC8hlt7lRyvVI9UeKXdQbV_OGJwam18DubGeM4qQa83yx69uZCE9B3ZTi4STj9CMrY8X2UDArXOLcvtHm8y77uaZdOK0QrJMEVvUphEa4fgdn8GAyr_rB20DV.ZQE05I1hsaFbyN0VMtf45vHs0Er0_XM0DI8qOlN7ZN93jt08GLZ8atrjQpzEK73UbU78Ii2kmw5fK3izoqh4; __gads=ID=1d0139e4445a136c:T=1732619424:RT=1732719417:S=ALNI_MbbnvZheRFAjwWvuVr6xk9BrRADuQ; __gpi=UID=00000f77c697b6d3:T=1732619424:RT=1732719417:S=ALNI_MYiS9xNoAwvypeGW1OA6MSlv6b2rQ; __eoi=ID=3d0b92b7951f3ccd:T=1732619424:RT=1732719417:S=AA-AfjbEWj8VyqToXUH5YA4jyR4D; cto_bundle=yZWMD19DJTJGc1VCWmowZUxpM0tRNHpvY2tKZlh4dDZuREJUQ2slMkZ1YWhZZXJvTG1McUh3bTJMNktwOVQyczJLU09iR2Y4cUkzdWxvbm5XZHJzejVPRjJlNjZMTzhGd0slMkY1YzVEeDZRNEpoMlZFTlE4TVhmVSUyRjZUcWZWVmVabFpYYkNueHNrRVZWMEV1T29QJTJGJTJGTm41RURDd1FzUGNQUmVZWSUyQlBiYzRJbk5HbyUyQm5qN3JRRTV4Z1hlT1VYJTJCSTlHSFUydHNOS0U1ZGpBQ0lDQVNMdVh5dWtyJTJGNFglMkJJUSUzRCUzRA; _ga_10H0RZ0TC8=GS1.1.1732719341.5.1.1732719709.0.0.0; _td=6772e6c9-8d8c-4ddb-8243-ad869927f779; _ga_CGRZHQ8KQD=GS1.1.1732719419.4.1.1732719710.60.0.0; FCNEC=%5B%5B%22AKsRol_ssg8gPdbI_yjRi2F6ko5vf3OBCSApGJeOg7u7BDM2j754ejT-nfBoAx0i79pbcUiS8NBrksiau6CA0ShXGPtB-BVqjfyKWLhQvfZ5NOSoxB5UvTInGy7WVhTYcME_J1qz-UNCyb___TuxPcQg6a7kh-jGhg%3D%3D%22%5D%5D'
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://newportmesamoms.com/',
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

response = requests.get('https://newportmesamoms.com/resources/summer-camp/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

title_name = 'Summer Camps 2024'

reviews_1 = soup.find_all('div', {'class': 'et_pb_text_inner'})

for page_ in reviews_1:
    paragraphs_1 = page_.find_all('p')
    # print(paragraphs_1)

    for p in paragraphs_1:
        name_element = p.find('a')
        name = name_element.text.strip() if name_element else ''
        a_tag = p.find('a')
        if a_tag:
            # name = a_tag.text
            url = a_tag['href']
            
            # # address = p.get_text(strip=True).replace(name, '').strip()
            # address = ', '.join(p.stripped_strings)
            # address = p.get_text(strip=True).replace(name, '').replace(url, '').strip()
            # # address = address if address else 'none'
            # # address = address.replace(name, '').strip()
            # address = address.lstrip(', ') 

            address = ', '.join(p.stripped_strings)

            # Hapus 'name' dan 'url' dari teks
            address = address.replace(name, '').replace(url, '').strip()

            # Atur default jika address kosong
            address = address if address else 'none'

            # Hapus koma di awal teks, jika ada
            address = address.lstrip(', ')

            results.append({
                'County':'Newport Mesa',
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
               
filename = f"_________{title_name}.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','url'])
    writer.writeheader()  
    writer.writerows(results)  

print(f"Data telah disimpan ke dalam file '{filename}'")

