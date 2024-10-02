from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.edge.options import Options

import csv
import time
from bs4 import BeautifulSoup as bs
import re


def setup_browser():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # chrome_options = Options()
    # chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--disable-extensions")

    # chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

    # browser = webdriver.Edge(options=chrome_options)
    # # browser = webdriver.Chrome(options=chrome_options)
    # browser.maximize_window()
    # return browser


    
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    return browser



def login_to_website(browser, email, password):
    browser.get("https://www.importinfo.com/login")
    wait = WebDriverWait(browser, 60)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(email)
    time.sleep(2)
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    pass_field.send_keys(password)    
    time.sleep(1)
    klikinput = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'form-check-input')))
    klikinput.click()
    time.sleep(2)
    pass_field.send_keys(Keys.RETURN)
    time.sleep(10)

def search_company(browser, company_name):
    browser.get('https://www.importinfo.com/search')
    time.sleep(3)
    search_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Search Our Database"]')))
    search_input.send_keys(company_name)
    time.sleep(3)
    search_input.send_keys(Keys.RETURN)

def read_data_from_page(browser, filename, fields):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    soup = bs(browser.page_source, 'html.parser')
    table = soup.find('table', class_='table table-striped table-sm mb-0')

    if table:
        rows = table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                last_col = cols[-1].find('a')
                if last_col and 'href' in last_col.attrs:
                    open_cols_link(browser, last_col['href'], filename, fields)

def open_cols_link(browser, href, filename, fields):
    browser.execute_script("window.open();")
    browser.switch_to.window(browser.window_handles[-1])
    browser.get(href)
    time.sleep(3)

    try:
        consignee_name_href = get_element_attribute(browser, "//th[text()='Consignee Name']/following-sibling::td/a", 'href')
    except:
        consignee_name_href = ''    
    
    consignee_name = get_element_text(browser, "//th[text()='Consignee Name']/following-sibling::td")
    exporter_name = get_element_text(browser, "//th[text()='Shipper Name']/following-sibling::td")
    port_of_Unlading_name_detail = get_element_text(browser, "//th[string()='Port of Unlading']/following-sibling::td")
    commodity_description = get_element_text(browser, "//th[text()='Commodity Description']/following-sibling::td")
    
    phone_number_Consignee, email_Consignee = extract_contact_info(browser, "//th[text()='Consignee Name']/ancestor::tr/following-sibling::tr[3]/td")
    _phone_number_Consignee_1, _email_Consignee_1 = extract_contact_info(browser, "//th[text()='Consignee Name']/ancestor::tr/following-sibling::tr[2]/td")
    _phone_number_Consignee_2, _email_Consignee_2 = extract_contact_info(browser, "//th[text()='Consignee Name']/ancestor::tr/following-sibling::tr[4]/td")

    
    
    phone_Consignee__1, email_Consignee__1 = extract_contact_info(browser, "//th[text()='Consignee Name']/ancestor::tbody/tr/th[text()='COMM Number']/following-sibling::td")
    
    notify_Party_Name = get_element_text(browser, "//th[text()='Notify Party Name']/following-sibling::td")
    address_Notify_Party = ' '.join(
        filter(None, [
            get_element_text(browser, "//th[text()='Notify Party Name']/ancestor::tr/following-sibling::tr[1]/td"),
            get_element_text(browser, "//th[text()='Notify Party Name']/ancestor::tr/following-sibling::tr[2]/td"),
            get_element_text(browser, "//th[text()='Notify Party Name']/ancestor::tbody/tr/th[text()='City']/following-sibling::td"),
            get_element_text(browser, "//th[text()='Notify Party Name']/ancestor::tbody/tr/th[text()='State Province']/following-sibling::td"),
            get_element_text(browser, "//th[text()='Notify Party Name']/ancestor::tbody/tr/th[text()='Country Code']/following-sibling::td")
        ])
    )
    
    phone_number_Party, email_Party = extract_contact_info(browser, "//th[text()='Notify Party Name']/ancestor::tr/following-sibling::tr[3]/td")
    _phone_number_Party_1, _email_Party_1 = extract_contact_info(browser, "//th[text()='Notify Party Name']/ancestor::tr/following-sibling::tr[2]/td")
    _phone_number_Party_2, _email_Party_2 = extract_contact_info(browser, "//th[text()='Notify Party Name']/ancestor::tr/following-sibling::tr[4]/td")

    phone_number__Party_1, email_Party_1 = extract_contact_info(browser, "//th[text()='Notify Party Name']/ancestor::tbody/tr/th[text()='COMM Number']/following-sibling::td")

    phone_numbers = []
    email_address = []
    address_consignee = ''


    if consignee_name_href:
        browser.get(consignee_name_href)
        time.sleep(5)
        try:
            phone_numbers = get_phone_numbers(browser, "//th[string()='Phone Number']/ancestor::table/tbody/tr/td[1]")
        except:
            phone_numbers =''
        try:
            email_address = get_phone_emails(browser, "//th[string()='Email Address']/ancestor::table/tbody/tr/td[1]")
        except:
            email_address = ''
        try:
            address_consignee = get_element_text(browser, "//th[string()='Address']//ancestor::table/tbody/tr[1]/td[2]")        
        except:
            address_consignee = ''

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    importinfo = {
        'Exporter Name': exporter_name,
        'Consignee Name': consignee_name,
        'Consignee Details Email': ', '.join(filter(None, [email_Consignee, _email_Consignee_1, _email_Consignee_2, email_Consignee__1])),
        'Consignee Details Email 2': ', '.join(email_address),
        'Consignee Details Phone Number': "'"+', '.join(filter(None, [phone_number_Consignee, _phone_number_Consignee_1, _phone_number_Consignee_2,  phone_Consignee__1])),
        'Consignee Details Phone Number 2': "'"+', '.join(phone_numbers),
        'Consignee Address': address_consignee,
        'Purchased Item Details': commodity_description,
        'Country / port of destination': port_of_Unlading_name_detail,
        'Notify Party Name': notify_Party_Name,
        'Notify Party Address': address_Notify_Party,
        'Notify Party Email': "'"+', '.join(filter(None, [email_Party, email_Party_1, _email_Party_1, _email_Party_2])),
        'Notify Party Phone Number': "'"+', '.join(filter(None, [phone_number__Party_1, phone_number_Party, _phone_number_Party_1, _phone_number_Party_2])),
        'FUll Details URL': href,
        'Consignee name URL': consignee_name_href,
    }


    print('Saving', importinfo['Consignee Name'],importinfo['FUll Details URL'])
    save_to_csv(filename, fields, [importinfo])
    
def get_phone_numbers(browser, xpath):
    try:
        elements_phone = browser.find_elements(By.XPATH, xpath)
        return [element_phone.text.strip() for element_phone in elements_phone]
    except:
        return []

def get_phone_emails(browser, xpath):
    try:
        elements_emails = browser.find_elements(By.XPATH, xpath)
        return [element_email.text.strip() for element_email in elements_emails]
    except:
        return []

def extract_contact_info(browser, xpath):
    try:
        element_text = browser.find_element(By.XPATH, xpath).text.strip()
        phone_number = re.search(r'\+?\d[\d\s\-()]*', element_text)
        email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', element_text)
        return (phone_number.group() if phone_number else ' ',
                email.group() if email else ' ')
    except:
        return ' ', ' '

def get_element_text(browser, xpath):
    try:
        return browser.find_element(By.XPATH, xpath).text.strip()
    except:
        return ''

def get_element_attribute(browser, xpath, attribute):
    try:
        return browser.find_element(By.XPATH, xpath).get_attribute(attribute)
    except:
        return ''

def get_elements_text(browser, xpath):
    try:
        return [element.text.strip() for element in browser.find_elements(By.XPATH, xpath)]
    except:
        return []

def save_to_csv(filename, fields, data):
    file_exists = False
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

def click_pagination_links(browser, filename, fields):
    current_page = 1
    while True:
        print(f"Current Page: {current_page}")
        read_data_from_page(browser, filename, fields)
        try:
            time.sleep(5)
            current_page += 1
            next_button = browser.find_element(By.XPATH, f"//a[@class='page-link' and text()='{current_page}']")
            if next_button:
                time.sleep(3)
                next_button.click()
                time.sleep(5)
            else:
                break
        except Exception as e:
            print(f"Exception occurred: {e}")
            break


# def click_pagination_links(browser, filename, fields):
#     current_page = 1
#     try:
        
#         wait = WebDriverWait(browser, 20)
#         next_button = wait.until(
#             EC.presence_of_element_located((By.XPATH, f"//a[@class='page-link' and text()='{current_page}']"))
#         )
        
#         browser.execute_script("arguments[0].scrollIntoView(true);", next_button)
#         time.sleep(1)  
#         next_button.click()
#     except Exception as e:
#         print(f"Tombol untuk halaman ke-{current_page} tidak tersedia: {e}")
#         return
    
#     time.sleep(5)
    
#     while True:
#         print(f"Current Page: {current_page}")
#         read_data_from_page(browser, filename, fields)
#         try:
#             current_page += 1
#             next_button = browser.find_element(By.XPATH, f"//a[@class='page-link' and text()='{current_page}']")
#             if next_button:
#                 browser.execute_script("arguments[0].scrollIntoView(true);", next_button)
#                 time.sleep(1)
#                 next_button.click()
#                 time.sleep(5)
#             else:
#                 break
#         except Exception as e:
#             print(f"Exception occurred: {e}")
#             break

def main():
    EMAIL = "Max2020t@gmail.com"
    PASSWORD = "k8yLGK9$$NTFFM8"
    COMPANY_NAME = "CARPAYDIEM"
    FILENAME = f'exporters--{COMPANY_NAME}--------1.csv'
    FIELDS = ['Exporter Name', 'Consignee Name', 'Consignee Details Email', 'Consignee Details Email 2', 'Consignee Details Phone Number', 'Consignee Details Phone Number 2', 'Consignee Address', 'Purchased Item Details', 'Country / port of destination', 'Notify Party Name', 'Notify Party Address', 'Notify Party Email', 'Notify Party Phone Number', 'FUll Details URL', 'Consignee name URL']

    browser = setup_browser()
    # add_cookies(browser)
    login_to_website(browser, EMAIL, PASSWORD)
    search_company(browser, COMPANY_NAME)
    click_pagination_links(browser, FILENAME, FIELDS)
    browser.quit()

if __name__ == "__main__":
    main()
