import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv




cookies = {
    'cookie':'_ga=GA1.1.823657898.1732619417; _fbp=fb.1.1732619418980.751282899794716027; __td_signed=true; __td_blockEvents=false; pmc_atlasmg_id=45489b5b-9c69-41e1-8a4d-0999c093752c; cto_bundle=V3lQbV9DJTJGc1VCWmowZUxpM0tRNHpvY2tKZld1QlVPbVl2ZCUyQnZSVkxrRVJEdlJwZmdyTVVmUHNpTTY1QzdNY0FEclNjUFBxZyUyQlNxbGV5UVVDc1ZBWlRPNmhYa2g3ZiUyRkRwckdMM2hOZUV0JTJGTFVTQkdJM1NJU0Q1VnNtUlZ3c2hkRXlTRHdrdXZ2Tk1Bek1XcFlQQ2N6QzFsMlBsRE9tazVUaVlrek9uM2kybkdad0VRZWpnQ2p0TXhwQU43Y21YdGpaZ0Y2eTMyZ1ZNTldxSnlTVlNJQ1VxT2xBZyUzRCUzRA; MCPopupClosed=yes; permutive-id=3cedbd0b-0059-4c7d-b42d-d18fef29581c; cf_clearance=BBiidqw0VsM185pnWc80jnGwcWRUTHzrJ_Oiu3p9OmY-1732633236-1.2.1.1-4AC3uhDKOoQhdwzLQJO8QYg.8Swc7a2GnvlsQl8qGEC1cmBwOhftKDU4Gx8A1sKjA38Vg59XVAIIfGm9M85uYlzpWuRmrLE1F8bfYz36yJiYmWm25sM_rnqKNl2Qf1GWM3I6mouux1UYRp0.lib4DDBxOlXexu.WkZkdJzUZ.VzYd5dov0VuK6Pkt0.fKqTiaF._CBYEIQGisPmJz9.UId5gs82Qt6PlbgLMWzztkDCMMP5oyRv00ly4fEAtDvOcuSl4.Shnb3k6RPfBA6dmB7bsjSpKROLPzb6Ze_tkHky1YsDj1tVD0gzlpqmPlH6XCabG9anfJ_WE1PnNrmv5oeANnhocz4_VN8.eUjcVWq75HPW4rX_QktZWzQeyADwfTQyHpp6MPoKkdYGks5QMmkMm0rktWctUM6Cuf4h4jkQ; __gads=ID=1d0139e4445a136c:T=1732619424:RT=1732633248:S=ALNI_MbbnvZheRFAjwWvuVr6xk9BrRADuQ; __gpi=UID=00000f77c697b6d3:T=1732619424:RT=1732633248:S=ALNI_MYiS9xNoAwvypeGW1OA6MSlv6b2rQ; __eoi=ID=3d0b92b7951f3ccd:T=1732619424:RT=1732633248:S=AA-AfjbEWj8VyqToXUH5YA4jyR4D; _ga_10H0RZ0TC8=GS1.1.1732631353.4.1.1732633380.0.0.0; _td=6772e6c9-8d8c-4ddb-8243-ad869927f779; _ga_CGRZHQ8KQD=GS1.1.1732631382.3.1.1732633383.58.0.0; FCNEC=%5B%5B%22AKsRol_FROD-8z3I_jatmL9N2MztKlesKV9scFgwGTXa9jW4BgJPHdYz0oIj9PV-ib0Dl5jm4CE0228WqpXli2dxXWqEry-wfxzrNNydL3U6If6Ve3AXLZbAyl1lsN6oLB8DllISg4iXe573d-E5AcSPImAGTQFR8Q%3D%3D%22%5D%5D'
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

response = requests.get('https://newportmesamoms.com/resources/home-sweet-home-2/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

title_name = 'Home Sweet Home'

reviews_1 = soup.find_all('div', {'class': 'et_pb_toggle_content clearfix'})

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
               
filename = f"{title_name}.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','url'])
    writer.writeheader()  
    writer.writerows(results)  

print(f"Data telah disimpan ke dalam file '{filename}'")

