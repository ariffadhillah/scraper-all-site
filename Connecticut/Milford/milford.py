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
    browser.get("https://greenwichmoms.com/")
    time.sleep(5)  # Tunggu hingga halaman terbuka


    # Daftar cookie
    cookies = [
        {"name": "_fbp", "value": "fb.1.1733659353413.22289360196139250"},
        {"name": "_ga", "value": "GA1.1.1484717220.1733659301"},
        {"name": "cf_clearance", "value": ".MgvAtNZW4qN1nqvtSWamfhnrhOzp469kteXQRoAzIg-1734491889-1.2.1.1-XewKD5ZGOF4EAgKTYrKlquDus5kH_KsgUIZhXTfk1SBAj_0lK2FeJpmjPt8yA1sn2pP4Wj1RwVhOvPxchzGYQXUQOGwgBSfX7nMAjCQ1eMU3JWce88Og1NlP_fjsTW0xjWlQMtPgb51sg0IizR5ZGZNNyeuP2Mp08tUzaQhoci6pYCqE.ZxeJ5uxF8mM9S2243us1LsoSImhA8dS05F65WABqHZJDyVWmaaybAA_mK4ghHXnt2lGrxKcQRuOogcVW7mhIfSpx72Pto.pXLpGyLAVVXEYW_buyjvyG7B29GT.xHmk18JqXgL1MaKSy6vkZOyOnCEHMAGlvQ5xKmksOpQPcmPQB.ndwH15iXxWmbm8.pXXO7He.7xP.i7O5Gs90WmMpkQ9EJNF8y0Mmf0lnzRX3XnmJ.8La66puNoNjJY"},
        {"name": "__gads", "value": "ID=8cf9f47d08f05d09:T=1733659303:RT=1734492750:S=ALNI_MblqkIuPsDY1Qoi-FMchTlaZUIo6Q"},
        {"name": "__gpi", "value": "UID=00000f87854bbb97:T=1733659303:RT=1734492750:S=ALNI_MaYc0OvIhBVpVCIzIaXNLjatYPqdg"},
        {"name": "__eoi", "value": "ID=4429362af089dcf2:T=1733659303:RT=1734492750:S=AA-Afja78oH-WPz96BR5MLJumBAW"},
        # {"name": "_ga_F1VRNQ2LMP", "value": "GS1.1.1733557869.6.1.1733558618.0.0.0"},
    ]


    for cookie in cookies:
        browser.add_cookie(cookie)


    browser.refresh()
    time.sleep(5)

    return browser


def open_to_website(browser):
    results = []


    browser.get("https://greenwichmoms.com/resources/shopping-and-products/")
    time.sleep(10)


    page_source = browser.page_source


    soup = BeautifulSoup(page_source, "html.parser")

    results = []

    title_name = 'Shopping'
    
    # reviews_1 = soup.find_all('div', class_=['et_pb_tab et_pb_tab_0 clearfix', 'et_pb_tab et_pb_tab_1 clearfix', 'et_pb_tab et_pb_tab_2 clearfix','et_pb_tab et_pb_tab_3 clearfix','et_pb_tab et_pb_tab_4 clearfix','et_pb_tab et_pb_tab_5 clearfix','et_pb_tab et_pb_tab_6 clearfix','et_pb_tab et_pb_tab_7 clearfix','et_pb_tab et_pb_tab_8 clearfix','et_pb_tab et_pb_tab_9 clearfix','et_pb_tab et_pb_tab_10 clearfix','et_pb_tab et_pb_tab_11 clearfix','et_pb_tab et_pb_tab_12 clearfix','et_pb_tab et_pb_tab_12 clearfix','et_pb_tab et_pb_tab_13 clearfix','et_pb_tab et_pb_tab_14 clearfix','et_pb_tab et_pb_tab_15 clearfix','et_pb_tab et_pb_tab_16 clearfix','et_pb_tab et_pb_tab_17 clearfix','et_pb_tab et_pb_tab_18 clearfix','et_pb_tab et_pb_tab_19 clearfix','et_pb_tab et_pb_tab_20 clearfix','et_pb_tab et_pb_tab_21 clearfix'])

    reviews_1 = soup.find_all('div', class_=['et_pb_text_inner'])
    
    # reviews_1 = soup.find_all('div', class_=['et_pb_tab et_pb_tab_0 clearfix', 'et_pb_tab et_pb_tab_1 clearfix', 'et_pb_tab et_pb_tab_2 clearfix','et_pb_tab et_pb_tab_3 clearfix','et_pb_tab et_pb_tab_4 clearfix'])

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
                    'County':'Greenwich',
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


def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(50)
    browser.quit()


if __name__ == "__main__":
    main()