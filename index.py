import requests
from bs4 import BeautifulSoup
import csv
import re
import os 

# Function to process paragraphs and extract name, url, and address
def extract_info(paragraphs):
    results = []
    for p in paragraphs:
        strong_tag = p.find('strong')
        a_tag = p.find('a')
        em_tag = p.find('em')

        # Extract name, URL, and address based on tags
        if strong_tag and a_tag:
            name = strong_tag.text.strip()
            url = a_tag['href']
            address = em_tag.text.strip() if em_tag else p.text.replace(name, '').replace('Click', '').replace('here', '').strip()
            address = address.split('for more information.')[0].strip()

            results.append({
                'name': name,
                'url': url,
                'address': address
            })

        elif a_tag:  # For cases where only <a> tag is found
            name = a_tag.text
            url = a_tag['href']
            address = p.get_text(strip=True).replace(name, '').strip() or 'none'

            results.append({
                'name': name,
                'url': url,
                'address': address
            })

    return results

# Fetch the webpage
cookies = {
    '_fbp': 'fb.1.1727272184560.436269777395599014',
    '_ga': 'GA1.2.2085893758.1727272183',
    # Add other necessary cookies here
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://northernwestchestermoms.com/resources/attractions/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Process all reviews dynamically
# all_reviews = soup.find_all('div', {'class': 'et_pb_text_inner'})
all_reviews = soup.find_all('div', class_=['et_pb_tab_content'])

final_results = []
for i, review in enumerate(all_reviews):
    paragraphs = review.find_all('p')
    result = extract_info(paragraphs)
    final_results.extend(result)


title = "Attractions"

for result in final_results:
    result['Title'] = title 

safe_title = re.sub(r'[^\w\s-]', '-', title).replace(' ', '-')

# Buat folder jika belum ada
folder_name = 'Northern Westchester'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Simpan data ke file CSV dengan nama berdasarkan title di dalam folder
csv_file = f'{folder_name}/{safe_title}.csv'  # Gunakan '/' untuk pemisah folder
csv_columns = ['Title', 'name', 'url', 'address']
try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_results)

    print(f"Data berhasil disimpan ke '{csv_file}'")

except IOError:
    print("Terjadi kesalahan saat menyimpan file.")


for result in final_results:
    print(f"Title = {result['Title']}")  
    print(f"name = {result['name']}")
    print(f"url = {result['url']}")
    print(f"address = {result['address']}")
    print() 