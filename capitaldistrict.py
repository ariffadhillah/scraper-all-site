import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup




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
    'referer': 'https://capitaldistrictmoms.com/resources/',
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

response = requests.get('https://capitaldistrictmoms.com/resources/aquatics/',  cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = []

# benar 1

reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})[0]
paragraphs_1 = reviews_1.find_all('p')
# print(paragraphs)



for p in paragraphs_1:
    a_tag = p.find('a')
    if a_tag:
        name = a_tag.text
        url = a_tag['href']
        # Ambil alamat jika ada
        address = p.get_text(strip=True).replace(name, '').strip()
        address = address if address else 'none'

        results.append({
            'name': name,
            'url': url,
            'address': address
        })



# Temukan semua elemen <p> di dalam div
reviews_2 = soup.find_all('div', {'class': 'et_pb_tab_content'})[1]
paragraphs_2 = reviews_2.find_all('p')



for p in paragraphs_2:
    strong_tag = p.find('strong')
    a_tag = p.find('a')
    em_tag = p.find('em')

    if strong_tag and a_tag:
        name = strong_tag.text.strip()
        url = a_tag['href']
        address = em_tag.text.strip() if em_tag else 'none'

        results.append({
            'name': name,
            'url': url,
            'address': address
        })




# 3

reviews_3 = soup.find_all('div', {'class': 'et_pb_tab_content'})[2]
paragraphs_3 = reviews_3.find_all('p')




for p in paragraphs_3:
    strong_tag = p.find('strong')
    a_tag = p.find('a')
    if strong_tag and a_tag:
        name = strong_tag.text.strip()
        url = a_tag['href']
        # Mengambil teks di antara elemen <strong> dan <a> sebagai alamat
        address = p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
        address = address.split('for more information.')[0].strip()

        results.append({
            'name': name,
            'url': url,
            'address': address
        })


reviews_4 = soup.find_all('div', {'class': 'et_pb_tab_content'})[3]
paragraphs_4 = reviews_4.find_all('p')
# print(paragraphs)


for p in paragraphs_4:
    a_tag = p.find('a')
    if a_tag:
        name = a_tag.text
        url = a_tag['href']
        # Ambil alamat jika ada
        address = p.get_text(strip=True).replace(name, '').strip()
        address = address if address else 'none'

        results.append({
            'name': name,
            'url': url,
            'address': address
        })

reviews_5 = soup.find_all('div', {'class': 'et_pb_tab_content'})[4]
paragraphs_5 = reviews_5.find_all('p')
# print(paragraphs)

# Inisialisasi daftar untuk menyimpan hasil


for p in paragraphs_5:
    a_tag = p.find('a')
    if a_tag:
        name = a_tag.text
        url = a_tag['href']
        # Ambil alamat jika ada
        address = p.get_text(strip=True).replace(name, '').strip()
        address = address if address else 'none'

        results.append({
            'name': name,
            'url': url,
            'address': address
        })


# Tampilkan hasil
for result in results:
    print(f"name = {result['name']}")
    print(f"url = {result['url']}")
    print(f"addres = {result['address']}")
    print()  # Untuk pemisah antar entri