# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.edge.options import Options

# import csv
# import time
# from bs4 import BeautifulSoup as bs
# import re


# def setup_browser():

#     chrome_options = Options()
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_argument("start-maximized")
#     chrome_options.add_argument("--disable-extensions")

#     # chrome_options = Options()
#     # chrome_options.add_argument("--disable-infobars")
#     # chrome_options.add_argument("start-maximized")
#     # chrome_options.add_argument("--disable-extensions")

#     chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

#     # browser = webdriver.Edge(options=chrome_options)
#     # # browser = webdriver.Chrome(options=chrome_options)
#     # browser.maximize_window()
#     # return browser


#     cookies = [
#             {"name": "_fbp", "value": "fb.1.1732807560072.127223409596317120"},
#             {"name": "_ga", "value": "GA1.1.921290859.1732807560"},
#             {"name": "cf_clearance", "value": "LAwOhtuPZ5ogKoDYel6VbClaCP1ZoGyoNLUwl0AB2g8-1732976434-1.2.1.1-yH_g0hDEiNlBQYZm0CMhtc1REd.hz1ruvB_Ne7mZyteepXrsCeJdsmnFoP6qIQX1nTZO60384w_Wb86MqfNWk.9mXfCNRYgkq6_qR8cHJmAoA4xElCp4aroPajTwhJz3vyhE1Rb4gXaKhJ4Ozt2J_ouv4Lf1YDx_PjSisDDqMQolDNN9nD6KEmNpyXiJQv8u6qIgtMUNOrNcQv4rwGo5YzbCeHIpJ6gZMMiSCvpmtTRHp_Bv425jNUXatM1QHpX1PdCga4V6YF7R1lE_53hwkBPcdHowZbNkti0R_rf.xHQO0tXUZvv.5DPhzYMkQMXfY3EXarjbGZq0mpL6zSpszq8Gfesiknz.TUdqbppH8Rx9cbIP51s_zM60a1z4mxZb1a.l2EBLcRor0QJXk2rcVVYLMcvU3ur__Wpe1o1zsz4jLHD8Ep0YN4hbNRzUfAax"},
#             {"name": "__gads", "value": "ID=9f9b30f5fdd0f87a:T=1732807554:RT=1732976440:S=ALNI_MaiKATCq-L6Euewxc8tHLUUs6jUFg"},
#             {"name": "__gpi", "value": "UID=00000f798b4a11e7:T=1732807554:RT=1732976440:S=ALNI_MZi6trZhZLMBxNv94Fsf4nVI9gqUQ"},
#             {"name": "__eoi", "value": "ID=9a4445b84edfae85:T=1732807554:RT=1732976440:S=AA-AfjaoAay7SoIMPviMKhYL4vtR"},
#             {"name": "_ga_N9HWH8N387", "value": "GS1.1.1732974113.7.1.1732976449.0.0.0"},
#         ]

#         # Menambahkan cookie satu per satu
#     for cookie in cookies:
#         browser.add_cookie(cookie)


    
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.maximize_window()
#     return browser


# def open_to_website(browser):
#     browser.get("https://thenorthcountymoms.com/auto-transport/")
#     time.sleep(10)




# def main():
#     browser = setup_browser() 
#     open_to_website(browser)
#     # time.sleep(50)
#     browser.quit()

# if __name__ == "__main__":
#     main()

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
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )

    # Inisialisasi browser
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    # Buka halaman awal (wajib sebelum menambahkan cookie)
    browser.get("https://thenorthcountymoms.com/")
    time.sleep(5)  # Tunggu hingga halaman terbuka


    # Daftar cookie
    cookies = [
        {"name": "_fbp", "value": "fb.1.1732807560072.127223409596317120"},
        {"name": "_ga", "value": "GA1.1.921290859.1732807560"},
        {"name": "cf_clearance", "value": "t7x0x5USNTUjqtYVaco_kOwoqiJZU1OOo9d4dQaGZV0-1733011665-1.2.1.1-qBecuDYDyn7n2w15e5wbq7okB1WalWolNWQPC2xK5FT8EwyaT1qpmV9rM5QjixM3FT6TBofAWFUcIfvZzspMT2Ye.D043hGr2LNqm_Qv6CNkjnte5ZiIg8_jE79trV9tuRVHqyPKARAHD_oTbQRvXNQl4771HtZmoBgB1Q6gtyMbFrHYzQrEqT5P3JdVtWmkCIKlEK_bF7ZabmyUUW7XI_g50gb72mUEzN7FHMTJUj90WwNppyBxGhp47u0z2My.MCwraTrFC3aKxcYjfLA1Lo3FYM335yMOA6rDIysBMkT0jvnUdtxePafsPtVnG0HRu7AfoNaFZfsxFk8hxeIshoIJQNm7Z1Q6RZgdv4AypiK2SQE8qIk0LiurfLWt.KfL4BNYHCw1fZstdwLKKchiGtvbCrFxWfPikAR0OkfiBE8L_T6IrPPXUhE2404gCLxn"},
        {"name": "__gads", "value": "ID=9f9b30f5fdd0f87a:T=1732807554:RT=1733011672:S=ALNI_MaiKATCq-L6Euewxc8tHLUUs6jUFg"},
        {"name": "__gpi", "value": "UID=00000f798b4a11e7:T=1732807554:RT=1733011672:S=ALNI_MZi6trZhZLMBxNv94Fsf4nVI9gqUQ"},
        {"name": "__eoi", "value": "ID=9a4445b84edfae85:T=1732807554:RT=1733011672:S=AA-AfjaoAay7SoIMPviMKhYL4vtR"},
        {"name": "_ga_N9HWH8N387", "value": "GS1.1.1733011670.9.1.1733011706.0.0.0"},
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

    title_name = 'Malls + Shops + Eats'
    # Kunjungi kembali URL target setelah cookie diterapkan
    browser.get("https://thenorthcountymoms.com/local-malls/")
    time.sleep(10)

    # Ambil sumber halaman (HTML)
    page_source = browser.page_source

    # Parsing dengan BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Temukan elemen dengan kelas `et_pb_tab_content`
    # tab_content_elements = soup.find_all("div", class_="et_pb_tab_content")


    reviews_1 = soup.find_all('div', {'class': 'et_pb_tab_content'})

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
                    'County':'North County',
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


def main():
    browser = setup_browser()
    open_to_website(browser)
    time.sleep(50)
    browser.quit()


if __name__ == "__main__":
    main()
