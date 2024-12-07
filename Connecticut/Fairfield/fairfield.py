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
    browser.get("https://fairfieldctmoms.com/")
    time.sleep(5)  # Tunggu hingga halaman terbuka


    # Daftar cookie
    cookies = [
        {"name": "_fbp", "value": "fb.1.1733445962427.912197316380830365"},
        {"name": "_ga", "value": "GA1.1.804256592.1733445962"},
        {"name": "cf_clearance", "value": "g2FDNviaoha8YVdYKt43w3OA.nacCcQydfjmOV2ZwYo-1727279461-1.2.1.1-h0PXEtZMtBkncTrthRi9uKLoO7bxO_t98Z7dui0Nn01Ny7VTXZenvCRmtFzjwXoila8et8LOjwVLd_OinW5YpNm0zZ73Ogp8Mivg_EKPPYvi5t2i2c5SJvaeYNkQmsbOzT6rtcoIDAA3YNzLXwQHiP9eQRK.S2ti4wowp.5nApEz0RLcd6n1cMLwRE.zXnIaScA2FXGeTJ4v0f11pawRfv0iOJZUEFi68DdLK.vWoppK06qwnJc__uPbPGgFS2qKlFlXJvy_9hU7FzpsNOC6QE288Z7.FscL_qPV.sQWW98cvqXexTy1zvITejs36KPNQgjbaGbvrdNMj9BpRRab9ZhYX.3.v.awMw1fLJa4aJemQhJEndlBphXQXK0xizkKCChVuZTvJgJgmLbkt_DI.vpeM4Nw3M2TUtFlO0Y1yK0"},
        {"name": "__gads", "value": "ID=085f3a3b20b61c08:T=1733445963:RT=1733558620:S=ALNI_MZn46y65AO24-UxUXuczosj6zjQEA"},
        {"name": "__gpi", "value": "UID=00000f84df21816b:T=1733445963:RT=1733558620:S=ALNI_MYRvs6JoOYQmQ0tScujaSKfHUQnPQ"},
        {"name": "__eoi", "value": "ID=d0041aa71a542439:T=1733445963:RT=1733558620:S=AA-Afjb1epeoHDWBYuiRpjpL7XKN"},
        {"name": "_ga_F1VRNQ2LMP", "value": "GS1.1.1733557869.6.1.1733558618.0.0.0"},
    ]


    for cookie in cookies:
        browser.add_cookie(cookie)


    browser.refresh()
    time.sleep(5)

    return browser


def open_to_website(browser):
    results = []


    browser.get("https://fairfieldctmoms.com/resources/sports/")
    time.sleep(10)


    page_source = browser.page_source


    soup = BeautifulSoup(page_source, "html.parser")


    output_ = 'Sports'

    divs = soup.find_all('div', class_='et_pb_tab_content')


    data = []

    for div in divs:
        current_entry = {}
        for p in div.find_all('p'):
            text = p.get_text(strip=True)
            link = p.find('a')
            href = link['href'] if link else None

            if href:

                if current_entry:
                    data.append(current_entry)
                    current_entry = {}

                current_entry['Name'] = text
                current_entry['Url'] = href

            elif text and text != '\xa0':  
                if 'Address' not in current_entry:
                    current_entry['Address'] = text
                else:
                    current_entry['Address'] += f", {text}"


        if current_entry:
            data.append(current_entry)

    for result in data:
        print(f"Name = {result.get('Name', 'N/A')}")
        print(f"Address = {result.get('Address', 'N/A')}")
        print(f"Url = {result.get('Url', 'N/A')}")
        print()




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