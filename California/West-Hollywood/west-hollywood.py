import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv


import requests
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import csv


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup



def setup_browser():
    # Konfigurasi Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")

    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')


    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )

    # Inisialisasi browser
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    # Buka halaman awal (wajib sebelum menambahkan cookie)
    browser.get("https://thewesthollywoodmoms.com/")
    time.sleep(5)  # Tunggu hingga halaman terbuka


    # Daftar cookie
    cookies = [
        {"name": "_fbp", "value": "fb.1.1732807560072.127223409596317120"},
        {"name": "_ga", "value": "GA1.1.921290859.1732807560"},
        {"name": "cf_clearance", "value": "8H8azDgUrjOyOJAVcc7l8BfQprTZcY81kjXS4r6c4us-1733013553-1.2.1.1-JVhrBgAl8uIvncDdvlsSkZnzEi3zej4tX24xA7aZBwZb5ZFLdl38TxAhzabjsbs3DeE8.7EM6TuZJpycNYWkSFXAlkrkNSzGnH2y421ZYOLZteuuwaFo6Ioa6GPJXAAbURmUpesWkFLVLQ1szmdc4kiYbT96EU6xekVhDWXWW1e.U51azJtJxM8wifpJZFc_hpMtomV3P.8xlsDAOLK3iE7SCWd245RE5AdSINRmoXGYazA7VNEns.dGWm9Qmh4DhyNEmmJRqqfoq27vOotp0.duEqA_SiAmaOxPkTvIHzx7gdwLL2zyHI1aN_d3JHsxMyVCL3M.Gjvm478_UgZXmsAOcSkZu5rMDdayQaoEJz1wX2s.qKOm2bm0vhlMaB1shzrEa.IbSZYwOZRq26AyeFCW8lKFKZNrGcoKUo.1o6avifrBv_otSWTBUkEGmNGz"},
        {"name": "__gads", "value": "ID=9f9b30f5fdd0f87a:T=1732807554:RT=1733013280:S=ALNI_MaiKATCq-L6Euewxc8tHLUUs6jUFg"},
        {"name": "__gpi", "value": "UID=00000f798b4a11e7:T=1732807554:RT=1733013280:S=ALNI_MZi6trZhZLMBxNv94Fsf4nVI9gqUQ"},
        {"name": "__eoi", "value": "ID=9a4445b84edfae85:T=1732807554:RT=1733013280:S=AA-AfjaoAay7SoIMPviMKhYL4vtR"},
        {"name": "_ga_N9HWH8N387", "value": "GS1.1.1733011670.9.1.1733013575.0.0.0"},
    ]

    # Menambahkan cookie ke browser
    for cookie in cookies:
        browser.add_cookie(cookie)

    # Refresh browser untuk menerapkan cookie
    browser.refresh()
    time.sleep(5)

    return browser


def open_to_website(browser):
    results = []

    # title_name = 'Wellness'
    # Kunjungi kembali URL target setelah cookie diterapkan
    browser.get("https://thewesthollywoodmoms.com/resources/dentists/")
    time.sleep(10)

    # Ambil sumber halaman (HTML)
    page_source = browser.page_source

    # Parsing dengan BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Temukan elemen dengan kelas `et_pb_tab_content`
    # tab_content_elements = soup.find_all("div", class_="et_pb_tab_content")

# Mencari semua <div> dengan kelas tertentu
    output_ = 'Dentists'

    divs = soup.find_all('div', class_='et_pb_toggle_content clearfix')

    # Menyimpan data dalam bentuk list of dictionaries
    data = []

    for div in divs:
        current_entry = {}
        for p in div.find_all('p'):
            text = p.get_text(strip=True)
            link = p.find('a')
            href = link['href'] if link else None

            if href:
                # Jika sudah ada entry sebelumnya, simpan ke data
                if current_entry:
                    data.append(current_entry)
                    current_entry = {}

                current_entry['Name'] = text
                current_entry['Url'] = href

            elif text and text != '\xa0':  # Abaikan elemen kosong
                if 'Address' not in current_entry:
                    current_entry['Address'] = text
                else:
                    current_entry['Address'] += f", {text}"

        # Tambahkan entry terakhir jika ada
        if current_entry:
            data.append(current_entry)

    for result in data:
        print(f"Name = {result.get('Name', 'N/A')}")
        print(f"Address = {result.get('Address', 'N/A')}")
        print(f"Url = {result.get('Url', 'N/A')}")
        print()



    # Simpan ke dalam file CSV
    csv_file = f'{output_}.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['County','Title','Name','Address', 'Contact', 'Email','Url'])
        writer.writeheader()
        writer.writerows(data)



def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(50)
    browser.quit()


if __name__ == "__main__":
    main()

