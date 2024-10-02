# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # import base64


# # cookies = {
# #     '_fbp': 'fb.1.1727272184560.436269777395599014',
# #     'pmc_atlasmg_id': '6386ac4a-a262-4608-9ae6-29a626576ef4',
# #     '__td_signed': 'true',
# #     '__td_blockEvents': 'false',
# #     'permutive-id': '39c0a8c6-a3af-45d4-a59c-c2e27e0f6f3f',
# #     '_gid': 'GA1.2.663785626.1727272196',
# #     '_lr_env_src_ats': 'false',
# #     'MCPopupClosed': 'yes',
# #     '_cc_id': 'a3b14cffeb8408c4ae5b7a6c5e63dfb0',
# #     '_au_1d': 'AU1D-0100-001727272209-HTUZS66X-90GX',
# #     'cnx_userId': 'd8c3b48797c34355b9714708a829e3f9',
# #     'cto_bundle': 'Sz7GOV9qZ3RvMXZEcGFzUkxyVld3TG5DbWRSWjVGZnhRTzBrSWcyTm1vU3FFTkdsTnhRQW00N3g3Z2dzOGdTUkpKWHNwRXBpcVBBRHlwNHclMkJqWURCTUhNUnhIZ08lMkIwT2paaTlxU3lHQ1ZQYThQNnpPb280TXkxaU1tRlZ2Rk43c2dpWFU5RGlSMTFVaVBPQ2xoUDc3UE1pQnIyemM5QWVkWWQyNnZ6WTJLWXFZNCUyRmsxJTJGeDhqS0FTZE1TQkpIQzRoS3RXWUVweFFablhrRnJnR2ZicVNsYm9qWEl2aHdacm5oUlVGeFdPdTdXMUNqWFRadXNmSVFPM0d5Mnd6bllPcmRvUFRmMUJ2bFI1RlR2RjdJVkZ0QUQzajFRJTNEJTNE',
# #     'panoramaId_expiry': '1727447251631',
# #     'panoramaId': '7af3c29c7343d92fb110e7ffab88a9fb927a716dcbe4da8427adccf9942e1ac6',
# #     'panoramaIdType': 'panoDevice',
# #     '_lr_geo_location': 'ID',
# #     '_lr_retry_request': 'true',
# #     '_ga_FVWZ0RM4DH': 'GS1.1.1727362705.8.1.1727364712.60.0.0',
# #     '_td': '2a6790df-39c0-42d9-8016-3cfdb1192196',
# #     '_ga_CGRZHQ8KQD': 'GS1.1.1727362653.9.1.1727364720.52.0.0',
# #     'FCNEC': '%5B%5B%22AKsRol-4A16SdZUFY5Aux8AtUM5iWpIQ3EOD_h0fOKrYb558DGuNQ3rfII1bP-gtfWMrPaOcU2JgHw8KCw15EO-iSOrlf_DZ55SaeUG3bwRdJciiBQ8OVfLwBYxch2GOi05l3LUu-azMsp1ODnlSFZRR4VK34BNtcQ%3D%3D%22%5D%5D',
# #     '_ga': 'GA1.2.2085893758.1727272183',
# #     '_ga_5ED67KSQBC': 'GS1.1.1727362650.10.1.1727364852.0.0.0',
# #     '__gads': 'ID=8d6f27282db3f50a:T=1727272191:RT=1727366371:S=ALNI_MYi7pEkmbroxZltFLrAGZ68v6cLfw',
# #     '__gpi': 'UID=00000f1d8dcf0af8:T=1727272191:RT=1727366371:S=ALNI_MaS7c4i-q7xJOkVTbEANAy3uou1xA',
# #     '__eoi': 'ID=fb7eef1506f18bb2:T=1727272191:RT=1727366371:S=AA-AfjZd_iRTnHVNAsLekeeHMEi2',
# # }

# # headers = {
# #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #     'accept-language': 'en-US,en;q=0.9,id;q=0.8',
# #     'cache-control': 'max-age=0',
# #     # 'cookie': '_fbp=fb.1.1727272184560.436269777395599014; pmc_atlasmg_id=6386ac4a-a262-4608-9ae6-29a626576ef4; __td_signed=true; __td_blockEvents=false; permutive-id=39c0a8c6-a3af-45d4-a59c-c2e27e0f6f3f; _gid=GA1.2.663785626.1727272196; _lr_env_src_ats=false; MCPopupClosed=yes; _cc_id=a3b14cffeb8408c4ae5b7a6c5e63dfb0; _au_1d=AU1D-0100-001727272209-HTUZS66X-90GX; cnx_userId=d8c3b48797c34355b9714708a829e3f9; cto_bundle=Sz7GOV9qZ3RvMXZEcGFzUkxyVld3TG5DbWRSWjVGZnhRTzBrSWcyTm1vU3FFTkdsTnhRQW00N3g3Z2dzOGdTUkpKWHNwRXBpcVBBRHlwNHclMkJqWURCTUhNUnhIZ08lMkIwT2paaTlxU3lHQ1ZQYThQNnpPb280TXkxaU1tRlZ2Rk43c2dpWFU5RGlSMTFVaVBPQ2xoUDc3UE1pQnIyemM5QWVkWWQyNnZ6WTJLWXFZNCUyRmsxJTJGeDhqS0FTZE1TQkpIQzRoS3RXWUVweFFablhrRnJnR2ZicVNsYm9qWEl2aHdacm5oUlVGeFdPdTdXMUNqWFRadXNmSVFPM0d5Mnd6bllPcmRvUFRmMUJ2bFI1RlR2RjdJVkZ0QUQzajFRJTNEJTNE; panoramaId_expiry=1727447251631; panoramaId=7af3c29c7343d92fb110e7ffab88a9fb927a716dcbe4da8427adccf9942e1ac6; panoramaIdType=panoDevice; _lr_geo_location=ID; _lr_retry_request=true; _ga_FVWZ0RM4DH=GS1.1.1727362705.8.1.1727364712.60.0.0; _td=2a6790df-39c0-42d9-8016-3cfdb1192196; _ga_CGRZHQ8KQD=GS1.1.1727362653.9.1.1727364720.52.0.0; FCNEC=%5B%5B%22AKsRol-4A16SdZUFY5Aux8AtUM5iWpIQ3EOD_h0fOKrYb558DGuNQ3rfII1bP-gtfWMrPaOcU2JgHw8KCw15EO-iSOrlf_DZ55SaeUG3bwRdJciiBQ8OVfLwBYxch2GOi05l3LUu-azMsp1ODnlSFZRR4VK34BNtcQ%3D%3D%22%5D%5D; _ga=GA1.2.2085893758.1727272183; _ga_5ED67KSQBC=GS1.1.1727362650.10.1.1727364852.0.0.0; __gads=ID=8d6f27282db3f50a:T=1727272191:RT=1727366371:S=ALNI_MYi7pEkmbroxZltFLrAGZ68v6cLfw; __gpi=UID=00000f1d8dcf0af8:T=1727272191:RT=1727366371:S=ALNI_MaS7c4i-q7xJOkVTbEANAy3uou1xA; __eoi=ID=fb7eef1506f18bb2:T=1727272191:RT=1727366371:S=AA-AfjZd_iRTnHVNAsLekeeHMEi2',
# #     'dnt': '1',
# #     'priority': 'u=0, i',
# #     'referer': 'https://capitaldistrictmoms.com/resources/childrens-activities/',
# #     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
# #     'sec-ch-ua-mobile': '?0',
# #     'sec-ch-ua-platform': '"Windows"',
# #     'sec-fetch-dest': 'document',
# #     'sec-fetch-mode': 'navigate',
# #     'sec-fetch-site': 'same-origin',
# #     'sec-fetch-user': '?1',
# #     'upgrade-insecure-requests': '1',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
# # }

# # response = requests.get('https://capitaldistrictmoms.com/resources/childrens-activities/', cookies=cookies, headers=headers)
# # response = requests.request("GET", url, headers=headers, data=payload)

# # print(response.text)




# import requests
# from bs4 import BeautifulSoup

# url = "https://capitaldistrictmoms.com/wp-json/wp/v2/pages/124"

# payload = {}
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,id;q=0.8',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_fbp=fb.1.1727272184560.436269777395599014; pmc_atlasmg_id=6386ac4a-a262-4608-9ae6-29a626576ef4; __td_signed=true; __td_blockEvents=false; permutive-id=39c0a8c6-a3af-45d4-a59c-c2e27e0f6f3f; _gid=GA1.2.663785626.1727272196; _lr_env_src_ats=false; MCPopupClosed=yes; _cc_id=a3b14cffeb8408c4ae5b7a6c5e63dfb0; _au_1d=AU1D-0100-001727272209-HTUZS66X-90GX; cnx_userId=d8c3b48797c34355b9714708a829e3f9; cto_bundle=Sz7GOV9qZ3RvMXZEcGFzUkxyVld3TG5DbWRSWjVGZnhRTzBrSWcyTm1vU3FFTkdsTnhRQW00N3g3Z2dzOGdTUkpKWHNwRXBpcVBBRHlwNHclMkJqWURCTUhNUnhIZ08lMkIwT2paaTlxU3lHQ1ZQYThQNnpPb280TXkxaU1tRlZ2Rk43c2dpWFU5RGlSMTFVaVBPQ2xoUDc3UE1pQnIyemM5QWVkWWQyNnZ6WTJLWXFZNCUyRmsxJTJGeDhqS0FTZE1TQkpIQzRoS3RXWUVweFFablhrRnJnR2ZicVNsYm9qWEl2aHdacm5oUlVGeFdPdTdXMUNqWFRadXNmSVFPM0d5Mnd6bllPcmRvUFRmMUJ2bFI1RlR2RjdJVkZ0QUQzajFRJTNEJTNE; panoramaId_expiry=1727447251631; panoramaId=7af3c29c7343d92fb110e7ffab88a9fb927a716dcbe4da8427adccf9942e1ac6; panoramaIdType=panoDevice; _lr_geo_location=ID; _lr_retry_request=true; _ga_FVWZ0RM4DH=GS1.1.1727362705.8.1.1727364712.60.0.0; _td=2a6790df-39c0-42d9-8016-3cfdb1192196; _ga_CGRZHQ8KQD=GS1.1.1727362653.9.1.1727364720.52.0.0; FCNEC=%5B%5B%22AKsRol-4A16SdZUFY5Aux8AtUM5iWpIQ3EOD_h0fOKrYb558DGuNQ3rfII1bP-gtfWMrPaOcU2JgHw8KCw15EO-iSOrlf_DZ55SaeUG3bwRdJciiBQ8OVfLwBYxch2GOi05l3LUu-azMsp1ODnlSFZRR4VK34BNtcQ%3D%3D%22%5D%5D; _ga=GA1.2.2085893758.1727272183; _ga_5ED67KSQBC=GS1.1.1727362650.10.1.1727364852.0.0.0; __gads=ID=8d6f27282db3f50a:T=1727272191:RT=1727366371:S=ALNI_MYi7pEkmbroxZltFLrAGZ68v6cLfw; __gpi=UID=00000f1d8dcf0af8:T=1727272191:RT=1727366371:S=ALNI_MaS7c4i-q7xJOkVTbEANAy3uou1xA; __eoi=ID=fb7eef1506f18bb2:T=1727272191:RT=1727366371:S=AA-AfjZd_iRTnHVNAsLekeeHMEi2',
#     'dnt': '1',
#     'priority': 'u=0, i',
#     'referer': 'https://capitaldistrictmoms.com/resources/childrens-activities/',
#     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# # Ambil teks dari respons
# response_text = response.text.strip()

# # Ganti <\/p> menjadi <p></p>
# formatted_text = response_text.replace('<\\/p>', '<p></p>').replace('<\/a>','<a>')


# # Gunakan BeautifulSoup untuk mem-parsing HTML
# soup = BeautifulSoup(formatted_text, 'html.parser')

# # Temukan semua elemen <p>
# paragraphs = soup.find_all('p')

# for p in paragraphs:
#     print(p)




import time
import undetected_chromedriver.v2 as uc

# Membuat objek ChromeOptions dan menambahkan argumen headless
options = uc.ChromeOptions()
options.add_argument('--headless')  # Menambahkan argumen headless secara eksplisit
options.add_argument('--disable-gpu')  # Tambahan untuk headless mode di beberapa OS

# Membuka browser menggunakan undetected_chromedriver dengan opsi
driver = uc.Chrome(options=options)

# Mengakses halaman yang memiliki Cloudflare challenge
driver.get('https://huntingtonsmithtownmoms.com/resources/family-dining/')

# Tunggu beberapa detik agar challenge Cloudflare selesai
time.sleep(10)

# Lanjutkan dengan navigasi setelah Cloudflare challenge
driver.get('https://huntingtonsmithtownmoms.com/resources/aquatics/')
time.sleep(5)

# Ambil sumber halaman setelah CAPTCHA
page_source = driver.page_source
print("Berhasil melewati Cloudflare dalam mode headless")

# Lanjutkan dengan proses scraping atau task lainnya
driver.quit()
