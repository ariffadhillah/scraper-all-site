import requests
from bs4 import BeautifulSoup
import csv
import re
import os

import pandas as pd





headers = {
    'cookie' : 'rr_u_cid=7rufzpUFQhGKytFnqvaSyg; osano_consentmanager_uuid=5f410282-281a-4d69-8290-06a362e893f2; osano_consentmanager=ArmFJdOKN-V8ZNpVhVYWdynZjovn5QVov8Yke6Ga5apeYqKexweHYhKvB_amY-Ta89K16cXpx62TWwRAfPo6hssY6P3lAy_l1K9UbKSgz5jHH6CsfJ43Xl3iT7g0XCZbWojYK8au8XIIGKqX56oNQCU-oPnnpqr24FcVPmxA1_zXgPNt1-1E-Lgb1n4cFYmRYc8vFxWt9fPVlId54ShiQt8dSPm2Fsnb4zsCRJECQqf3jY_7uI3bmE8qHjA1_O0wmm0PP7C4PqBRxoM1n3t2cNmDFTcpYFAHUpxbY834LI24Pbk1IdcvvEtkfoWYfGTado2ZH6qW9Gw=; ajs_anonymous_id=b87893bc-f384-495a-84d4-7d598d864881; _ga=GA1.1.673643838.1729640718; FPAU=1.2.1623878839.1729640719; _gtmeec=e30%3D; _gcl_au=1.1.1033989149.1729640722; _fbp=fb.1.1729640722227.563386706210957647; _tt_enable_cookie=1; _ttp=l5xx5i8Jitr1g2-SD1ork64cvxR; age=19; _cfuvid=Mn_rI73VktS5q4nVKlS1w3Ew.h_ZFMRR6qYS4DERf2c-1729670959254-0.0.1.1-604800000; sid=H21q2DA6Sc2Ds0ShDbNTxQ; JSESSIONID=f36d8972-ecc0-44be-955e-48099f352bdc; __gtm_referrer=https%3A%2F%2Fwww.upwork.com%2F; __cf_bm=snZvmnkawn3AiDnRUKKRsJm_2f88iUUEVbq_bpY2eAc-1729672850-1.0.1.1-9L8lMQGo_xxlWgVQCQn7cMTJ1k9WuzR4dB9RIyvbdKJUWQkS5RWOl7WdKD0nfng_B5Gq2GDswnKgytGM_At8DLcDQQYNaVOr9mYMxJVpM8M; cf_clearance=ogv1SeIJhNzZtPDcvrrB02rUKanuoC59r6JTUbPKTHQ-1729673075-1.2.1.1-r7ILFN_yCnFxVT1iBgIOpAif4qAwmd4DTkD5FQfCG80ui42QqAhwxcOl4UxqclsENJpzel8rgwu.zON.Mt6kzjEchoKlg2xJMhj2XcnTyDmLA9_ERKYNpsNhsgrar5O1gQRQ_r_M9vHqNmu3hkWbq6GWlB_WkTW3OO1b1g2CH9DaR11aHgk85pXailM78XozGnR6cNUUcnuc.J1APSA.5DBwOQabZT7A04Q1hxYuXiDAtlzr3E6fLH_B.XapSrX8a8sWlTmnm1eU6r_tJtK5B4.BaGHjbkeF810F8mOzQS3n9F7A5zUuNGfxIZ0mfdr_xzZZa4t1_Wn2YzoNaO_ECAOuidJNtkODTwHWGpWbrJU15pq80cHBB7l.VVULK2EI; rv=[%221180425%22%2C%221049572%22%2C%222888625%22]; times={%22endDate%22:%2210/28/2024%22%2C%22endTime%22:%2210:00%22%2C%22startDate%22:%2210/25/2024%22%2C%22startTime%22:%2210:00%22}; _rdt_uuid=1729640717949.af544446-bf60-4339-90ca-a84592e08f70; preferredLocale=en-US; _uetsid=b3dc069090cf11ef80c5876ae9cafb76; _uetvid=b3dc755090cf11efbeade907b4408fac; _ga_CJPLS11T4Y=GS1.1.1729670963.2.1.1729673237.59.0.0; _ga_EWDCKE6BT8=GS1.1.1729670963.2.1.1729673237.0.0.1545595955',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

response = requests.get('https://turo.com/us/en/search?age=19&country=US&defaultZoomLevel=11&deliveryLocationType=city&endDate=10%2F28%2F2024&endTime=10%3A00&isMapSearch=false&itemsPerPage=200&latitude=33.7174708&location=Orange%20County%2C%20California%2C%20USA&locationType=CITY&longitude=-117.8311428&maximumPrice=&minimumPrice=100&pickupType=ALL&placeId=ChIJz_fVVFyS3IARB9bwj2HDpt4&region=CA&sortType=RELEVANCE&startDate=10%2F25%2F2024&startTime=10%3A00&useDefaultMaximumDistance=true', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

search = soup.find('div', class_='virtuoso-item-list')
print(search)