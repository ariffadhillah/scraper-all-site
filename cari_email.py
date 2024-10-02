import pandas as pd
import requests
import bs4
import re

# Membaca CSV input
src_df = pd.read_csv('capitaldistrictmoms/Aquatics.csv')

# Fungsi untuk memeriksa apakah URL memiliki skema (http/https)
def format_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'http://' + url  # Menambahkan 'http://' jika belum ada skema
    return url

# Fungsi untuk mendapatkan nomor telepon
# def get_phone(soup, response_text):
#     try:
#         phone = soup.select("a[href*=callto]")[0].text
#         return phone
#     except IndexError:
#         pass

#     try:
#         phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response_text)[0]
#         return phone
#     except IndexError:
#         pass

#     try:
#         phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response_text)[-1]
#         return phone
#     except IndexError:
#         print('Phone number not found')
#         return ''

# Fungsi untuk mendapatkan email
def get_email(soup, response_text):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response_text)[-1]
        return email
    except IndexError:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
        return email
    except IndexError:
        return ''

# Fungsi untuk mencari tautan 'contact', 'about', dll.
def find_additional_pages(soup, base_url):
    links = soup.find_all('a', href=True)
    keywords = ['contact-us','about-us', 'contact', 'about', 'contacts',  'how-to-help','Contact_Us']
    
    for link in links:
        href = link['href'].lower()
        if any(keyword in href for keyword in keywords):
            # Memastikan URL lengkap
            if not href.startswith('http'):
                href = base_url + href
            return href
    return None

# Loop untuk proses scraping
for i, row in src_df.iterrows():
    url = format_url(row['url'])
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f'Unsuccessful: {e}')
        continue

    # Mendapatkan phone dan email dari halaman utama
    # phone = get_phone(soup, response.text)
    email = get_email(soup, response.text)

    # Jika email tidak ditemukan di halaman utama, coba di halaman 'contact' atau 'about'
    if not email:
        additional_page = find_additional_pages(soup, url)
        if additional_page:
            try:
                response = requests.get(additional_page)
                response.raise_for_status()
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                email = get_email(soup, response.text)
                print(f'Checking additional page: {additional_page}')
            except requests.RequestException as e:
                print(f'Unsuccessful on additional page: {e}')

    # Menyimpan hasil ke DataFrame
    # src_df.loc[i, 'Phone'] = phone
    src_df.loc[i, 'Email'] = email
    print(f'website: {url}\nemail: {email}\n')
    src_df.to_csv('capitaldistrictmoms/hasil/hasil-Aquatics.csv', index=False)

# Menyimpan hasil akhir ke CSV
# src_df.to_csv('hasil_1.csv', index=False)
