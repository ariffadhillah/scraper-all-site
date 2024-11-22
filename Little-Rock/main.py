import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import re
import time


# Membaca CSV dari Google Sheets yang dipublikasikan
url_google_sheet_csv = "https://docs.google.com/spreadsheets/d/1BeH9lB_oCfb1qehK8QmgfOZIu55j6qQqvxoSXUIaFIA/gviz/tq?tqx=out:csv"
src_df = pd.read_csv(url_google_sheet_csv)

# Fungsi untuk memeriksa apakah URL memiliki skema (http/https) dan menghindari baris kosong
def format_url(url):
    if pd.isna(url):  # Memeriksa apakah URL kosong atau NaN
        return ''  # Jika kosong, kembalikan string kosong
    return url if url.startswith(('http://', 'https://')) else f'http://{url}'

# # Fungsi untuk mendapatkan email
# def get_email(soup):
#     # Mencari email dari teks biasa
#     email_matches = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', soup.text)
#     if email_matches:
#         return email_matches[-1]

#     # Mencari email dari link mailto
#     mailto_links = soup.select("a[href*=mailto]")
#     if mailto_links:
#         return mailto_links[-1]['href'].split(':')[1]

#     return ''

# Fungsi untuk mendapatkan email
def get_email(soup):
    # Mencari email dari teks biasa
    email_matches = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', soup.text)
    if email_matches:
        return email_matches[-1]

    # Mencari email dari link mailto
    mailto_links = soup.select("a[href*=mailto]")
    if mailto_links:
        return mailto_links[-1]['href'].split(':')[1]

    # Mencari email dalam elemen HTML seperti <p> dengan pola "Email: info@domain.com"
    email_paragraphs = soup.find_all('p', string=re.compile(r'Email:', re.IGNORECASE))
    for p in email_paragraphs:
        email_match = re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', p.text)
        if email_match:
            return email_match.group(1)

    return ''


# Fungsi untuk mencari tautan 'contact', 'about', dll.
def find_additional_pages(soup, base_url):
    keywords = ['Contact','Contact Us']
    links = soup.find_all('a', href=True)

    for link in links:
        href = link['href'].lower()
        if any(keyword in href for keyword in keywords):
            return href if href.startswith('http') else base_url + href
    return None


# Konfigurasi opsi Chrome untuk mode headless
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")



# Inisialisasi WebDriver dengan opsi yang dikonfigurasi
driver = webdriver.Chrome(options=chrome_options)

# Ubah nama kolom sesuai kebutuhan
src_df.columns = ['County','Title','Name','Address','Contact','Email','Url']

# Loop untuk memproses setiap baris dalam DataFrame
for i, row in src_df.iterrows():
    url = format_url(row['Url'])  # Panggil fungsi format_url untuk setiap baris
    if not url:  # Lewatkan baris jika URL kosong
        print(f'Skipping row {i}, empty URL')
        continue

    email = ''
    try:
        # Menggunakan Selenium untuk membuka halaman
        driver.get(url)
        time.sleep(2)  # Tunggu beberapa detik agar halaman termuat
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        email = get_email(soup)

        # Jika email tidak ditemukan di halaman utama, coba di halaman tambahan
        if not email:
            additional_page = find_additional_pages(soup, url)
            if additional_page:
                driver.get(additional_page)
                time.sleep(2)
                soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                email = get_email(soup)
                print(f'Checking additional page: {additional_page}')

    except Exception as e:
        print(f'Unsuccessful: {e} on {url}')
        continue

    # Menyimpan hasil ke DataFrame
    src_df.loc[i, 'Email'] = email
    print(f'website: {url}\nemail: {email}\n')

    # Simpan hasil setelah semua proses scraping selesai ke dalam folder Central NY dengan nama file berdasarkan title
    output_filename = 'hasil-scraping---1.csv'
    src_df.to_csv(output_filename, index=False)

# Tutup driver setelah selesai
driver.quit()


# # Loop untuk memproses setiap baris dalam DataFrame
# for i, row in src_df.iterrows():
#     url = format_url(row['Url'])  # Panggil fungsi format_url untuk setiap baris
#     if not url:  # Lewatkan baris jika URL kosong
#         print(f'Skipping row {i}, empty URL')
#         continue

#     email = ''
#     try:
#         # Menggunakan Selenium untuk membuka halaman
#         driver.get(url)
#         time.sleep(2)  # Tunggu beberapa detik agar halaman termuat
#         soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
#         email = get_email(soup)

#         # Jika email tidak ditemukan di halaman utama, coba di halaman tambahan
#         if not email:
#             additional_urls = find_additional_pages(url)
#             for additional_url in additional_urls:
#                 try:
#                     driver.get(additional_url)
#                     time.sleep(2)
#                     soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
#                     email = get_email(soup)
#                     print(f'Checking additional page: {additional_url}')
#                     if email:  # Berhenti jika email ditemukan
#                         break
#                 except Exception as inner_e:
#                     print(f"Error accessing {additional_url}: {inner_e}")
#                     continue

#     except Exception as e:
#         print(f'Unsuccessful: {e} on {url}')
#         continue

#     # Menyimpan hasil ke DataFrame
#     src_df.loc[i, 'Email'] = email
#     print(f'website: {url}\nemail: {email}\n')

#     # Simpan hasil setelah semua proses scraping selesai ke dalam folder Central NY dengan nama file berdasarkan title
#     output_filename = 'hasil-----.csv'
#     src_df.to_csv(output_filename, index=False)

# # Tutup driver setelah selesai
# driver.quit()
