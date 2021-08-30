
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time

import pandas as pd
import numpy as np


#웹드라이버 / URL 선언

driver = webdriver.Chrome()
url = 'https://search.shopping.naver.com/search/all?query=%EB%B0%94%EB%94%94%EC%9B%8C%EC%8B%9C&frm=NVSHATC'
driver.get(url)


# 현재 페이지에서 필요한 정보들을 받아보자
def jjim_file(url):
    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(4) # 무작정 기다리는게 아니라 조건 성립할때 까지만 기다리는거 확인

    price_list = []
    # 금액 가져오기
    price = driver.find_elements_by_css_selector('#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo >\
                                 div.style_content__2T20F > ul > div > div> li > div > div.basicList_info_area__17Xyo > div.basicList_price_area__1UXXR >\
                                 strong > span > span.price_num__2WUXn')

    # 금액 리스트화
    for pri in price :
        price_list.append(pri.text) #확인필요


    df = pd.DataFrame(list(zip(price_list)), columns = ['price'])
    print(df)
    df_done = df.sort_values(by=['price'], ascending=False)
    df_done = df_done.reset_index(drop=True)
    result_dict = df_done.to_dict('index')
    result_num = len(result_dict)
    print(result_dict)

        
    return result_dict, result_num


jjim_file(url)

def all_categories():
    cat_list = []
    여성_신발 = 'https://search.shopping.naver.com/search/category?catId=50000173&frm=NVSHCAT&origQuery&pagingIndex=1&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list'
    return cat_list

