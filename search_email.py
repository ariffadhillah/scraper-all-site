import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

import bs4
import re
import time

# Membaca CSV input
src_df = pd.read_csv('capitaldistrictmoms/Aquatics.csv')

# Fungsi untuk memeriksa apakah URL memiliki skema (http/https)
def format_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'http://' + url  # Menambahkan 'http://' jika belum ada skema
    return url

# Fungsi untuk mendapatkan nomor telepon
# def get_phone(soup):
#     try:
#         phone = soup.select("a[href*=callto]")[0].text
#         return phone
#     except IndexError:
#         pass

#     try:
#         phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', soup.text)[0]
#         return phone
#     except IndexError:
#         pass

#     try:
#         phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', soup.text)[-1]
#         return phone
#     except IndexError:
#         print('Phone number not found')
#         return ''

# Fungsi untuk mendapatkan email
# def get_email(soup):
#     try:
#         email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', soup.text)[-1]
#         return email
#     except IndexError:
#         pass

#     try:
#         email = soup.select("a[href*=mailto]")[-1].text
#         return email
#     except IndexError:
#         return ''

def get_email(soup):
    # Pertama, coba ambil email dari teks biasa
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', soup.text)[-1]
        return email
    except IndexError:
        pass

    # Kemudian, coba ambil email dari tag <a> dengan href yang mengandung 'mailto:'
    try:
        email_link = soup.select("a[href*=mailto]")[-1]['href']
        # Mengambil email dari href
        email = email_link.split(':')[1]  # Memisahkan string 'mailto:email@domain.com'
        return email
    except (IndexError, KeyError):
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

chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode headless (tanpa UI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920x1080")

# browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()


# Path ke ChromeDriver Anda (pastikan sudah terinstal)
# webdriver_service = Service('/path/to/chromedriver')  # Ganti dengan path ChromeDriver di sistem Anda
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Edge(options=chrome_options)
driver.maximize_window()

# Loop untuk proses scraping
for i, row in src_df.iterrows():
    url = format_url(row['url'])
    
    try:
        # Menggunakan Selenium untuk membuka halaman
        driver.get(url)
        time.sleep(1)  # Tunggu beberapa detik agar halaman termuat sempurna
        page_source = driver.page_source
        soup = bs4.BeautifulSoup(page_source, 'html.parser')
    except Exception as e:
        print(f'Unsuccessful: {e}')
        continue

    # Mendapatkan phone dan email dari halaman utama
    # phone = get_phone(soup)
    email = get_email(soup)

    # Jika email tidak ditemukan di halaman utama, coba di halaman 'contact' atau 'about'
    if not email:
        additional_page = find_additional_pages(soup, url)
        if additional_page:
            try:
                driver.get(additional_page)
                time.sleep(1)
                page_source = driver.page_source
                soup = bs4.BeautifulSoup(page_source, 'html.parser')
                email = get_email(soup)
                print(f'Checking additional page: {additional_page}')
            except Exception as e:
                print(f'Unsuccessful on additional page: {e}')

    # Menyimpan hasil ke DataFrame
    # src_df.loc[i, 'Phone'] = phone
    src_df.loc[i, 'Email'] = email
    print(f'website: {url}\nemail: {email}\n')
    src_df.to_csv('capitaldistrictmoms/hasil/Aquatics.csv', index=False)

# Menyimpan hasil akhir ke CSV
# src_df.to_csv('output.csv', index=False)

# Tutup driver setelah selesai
driver.quit()
