import pandas as pd
import requests
import bs4
import re

# Membaca CSV input
src_df = pd.read_csv('scraping_results.csv')

# Fungsi untuk memeriksa apakah URL memiliki skema (http/https)
def format_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'http://' + url  # Menambahkan 'http://' jika belum ada skema
    return url

# Fungsi untuk mendapatkan nomor telepon
def get_phone(soup, response_text):
    try:
        phone = soup.select("a[href*=callto]")[0].text
        return phone
    except IndexError:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response_text)[0]
        return phone
    except IndexError:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response_text)[-1]
        return phone
    except IndexError:
        print('Phone number not found')
        return ''

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
        print('Email not found')
        return ''

# Loop untuk proses scraping
for i, row in src_df.iterrows():
    url = format_url(row['url'])  # Memformat URL dengan fungsi format_url
    try:
        response = requests.get(url)
        response.raise_for_status()  # Menambahkan pengecekan jika request gagal
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f'Unsuccessful: {e}')
        continue

    # Mendapatkan phone dan email
    phone = get_phone(soup, response.text)
    email = get_email(soup, response.text)

    # Menyimpan hasil ke DataFrame
    src_df.loc[i, 'Phone'] = phone
    src_df.loc[i, 'Email'] = email
    print(f'website: {url}\nphone: {phone}\nemail: {email}\n')
    src_df.to_csv('output.csv', index=False)

# Menyimpan hasil akhir ke CSV
# src_df.to_csv('output.csv', index=False)
