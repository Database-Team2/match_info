import re
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crawler_matches(url, file_path):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome('C:/Users/SION_2/Downloads/chromedriver_win32/chromedriver', options=options)

    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mw-collapsible-text")))
    btns = driver.find_elements_by_class_name('mw-collapsible-text')
    print('총 경기수:', len(btns) - 1)
    for btn in btns:
        btn.click()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    matches = soup.select('.mw-collapsible-content > table > tbody')

    premier_db = {}
    premier_db['match_info'] = []
    count = 0
    for _ in matches:
        items = soup.select('tr')
        match_date = ''
        match_time = ''
        home_club = ''
        away_club = ''
        for i in range(len(items)):
            if count > 380:
                pprint(premier_db['match_info'])
                with open(file_path, 'w', encoding='utf-8') as outfile:
                    json.dump(premier_db, outfile, indent=4, ensure_ascii=False)
                return
            tmp = re.sub(r"\n", ",", items[i].text)
            if i % 4 == 0:
                count += 1
                try:
                    dates = re.search(r'\d{4}년 (\d|\d{2})월 (\d|\d{2})일', tmp).group()
                    dates = re.split(r'[년월일]', dates)
                    del dates[3]
                    dates[1] = re.sub(r'\s', '', dates[1])
                    dates[2] = re.sub(r'\s', '', dates[2])
                    dates[1] = dates[1].zfill(2)
                    dates[2] = dates[2].zfill(2)
                    match_date = ''.join(dates)

                    match_time = re.search(r'\d{2}:\d{2}', tmp).group()
                    # print('DATE:', match_date, 'TIME:', match_time)

                # 연기되어 무기한 연기된 경기
                except:
                    match_date = ''
                    match_time = ''
                    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', '진짜시간은', match_date, match_time)

            if i % 4 == 1:
                clubs = tmp.split(',,')
                clubs_a = []
                for i in range(3):
                    item = re.sub(r',', '', clubs[i])
                    clubs_a.append(item)
                home_club = clubs_a[0]
                away_club = clubs_a[2]
                # print('CLUBS:', home_club, ',', away_club)
                #
                # print('COUNT!', count)
                # print('----------------------------------------------')

            if i % 4 == 3:
                # print(count, match_date, match_time, home_club, ',', away_club)
                doc = {
                    'match_id': count,
                    'match_date': match_date,
                    'match_time': match_time,
                    'home_club': home_club,
                    'away_club': away_club,
                    'stadium': 3,
                }
                premier_db['match_info'].append(doc)




url = 'https://ko.wikipedia.org/wiki/%ED%94%84%EB%A6%AC%EB%AF%B8%EC%96%B4%EB%A6%AC%EA%B7%B8_2021-22_%EA%B2%BD%EA%B8%B0_%EC%9D%BC%EC%A0%95'
file_path = '../json_data/match_info.json'

crawler_matches(url, file_path)
