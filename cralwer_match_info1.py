import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime


def crawler_matches(url, premier_db):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    driver = webdriver.Chrome('C:/Users/SION_2/Downloads/chromedriver_win32/chromedriver')
    driver.get(url)
    sleep(4)
    btn = driver.find_element_by_class_name('_2hTJ5th4dIYlveipSEMYHH.BfdVlAo_cgSVjDUegen0F.js-accept-all-close')
    btn.click()
    for c in range(0, 25):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(0.2)
    sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    match_lists = soup.select('.matchList')

    for match_list in match_lists:
        matches = match_list.select('li')
        for match in matches:
            match_id = int(match['data-comp-match-item'])
            detail_url = 'https:' + match.select_one('div')['data-href']

            data = requests.get(detail_url, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            if soup.select_one('.team.home'):
                home_club_tag = soup.select_one('.team.home > a')['href']
                away_club_tag = soup.select_one('.team.away > a')['href']
                home_club_id = re.search(r'\d+', home_club_tag).group()
                away_club_id = re.search(r'\d+', away_club_tag).group()
            else:
                print('----번리 토트넘 무기한 연장----')
                home_club_id, away_club_id = 43, 21

            timestamp_tag = soup.select_one('.matchDate.renderMatchDateContainer')
            if timestamp_tag:
                timestamp = soup.select_one('.matchDate.renderMatchDateContainer')['data-kickoff']
                match_date = datetime.fromtimestamp(int(timestamp) // 1000).strftime('%Y%m%d')
            else:
                match_date = ''
            # print(match_id, match_date, home_club_id, away_club_id)
            doc = {
                'match_id': match_id,
                'match_date': match_date,
                'home_club_id': home_club_id,
                'away_club_id': away_club_id,
            }
            print(doc)
            premier_db['match_info'].append(doc)

    return premier_db


def main():
    url = 'https://www.premierleague.com/results'
    url1 = 'https://www.premierleague.com/fixtures'
    file_path = './match_info1.json'

    premier_db = {}
    premier_db['match_info'] = []
    crawler_matches(url, premier_db)
    crawler_matches(url1, premier_db)

    with open(file_path, 'w') as outfile:
        json.dump(premier_db, outfile, indent=4)


if __name__ == "__main__":
    main()
