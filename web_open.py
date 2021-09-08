
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import sql_code.pd_sql_direct_conn as db_conn #데이터 베이스에 넣기 위한 SQL문 작성파일
import datetime
import time

import pandas as pd
import numpy as np


#웹드라이버 / URL 선언

driver = webdriver.Chrome()
url = 'https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%EB%B0%94%EB%94%94%EC%9B%8C%EC%8B%9C'
driver.get(url)




# 검색어를 입력하고, 자동으로 입력결과 페이지를 출력하는 함수
def search_by_name(ask):
    elem = driver.find_element_by_class_name("searchInput_search_input__1Eclz")
    elem.clear()
    elem.send_keys(ask)
    driver.implicitly_wait(time_to_wait=5)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    result = elem.send_keys(Keys.RETURN)
    return result


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

    pn_list = []
    jj_list = []
    link_list = []
    price_list = []

    # 품목명 가져오기
    product_name = driver.find_elements_by_css_selector('#__next > div > div.style_container__1YjHN > div >\
                                div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div > li > div > div.basicList_info_area__17Xyo >\
                                div.basicList_title__3P9Q7 > a.basicList_link__1MaTN')
    # 품목명 리스트화
    for name in product_name:
        pn_list.append(name.text)


    # 찜하기 갯수 가져오기
    jjim_num = driver.find_elements_by_css_selector('#__next > div > div.style_container__1YjHN > div >\
                                div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div > li > div > div.basicList_info_area__17Xyo >\
                                div.basicList_etc_box__1Jzg6 > span.basicList_etc__2uAYO > button > span > em')
    # 찜하기 리스트화
    for num in jjim_num:
        real_num = num.text.replace(",","")        
        jj_list.append(int(real_num))

    # 이동링크 가져오기
    link_tag = driver.find_elements_by_css_selector('#__next > div > div.style_container__1YjHN > div >\
                                div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div > li > div > div.basicList_info_area__17Xyo >\
                                div.basicList_title__3P9Q7 > a.basicList_link__1MaTN')

    # 링크 리스트화
    for link in link_tag:
        link_list.append(link.get_attribute('href'))

    # 금액 가져오기
    price = driver.find_elements_by_css_selector('#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo >\
                                 div.style_content__2T20F > ul > div > div> li > div > div.basicList_info_area__17Xyo > div.basicList_price_area__1UXXR >\
                                 strong > span > span.price_num__2WUXn')

    # 금액 리스트화
    for pri in price :
        price_list.append(pri.text) #확인필요

    # 조회기준 시간 열 추가


    # 데이터 추출 기준 시간 추가
    mask = '%Y%m%d'
    now = datetime.datetime.now().strftime(mask)

    df = pd.DataFrame(list(zip(pn_list,jj_list, price_list, link_list)), columns = ['Name','jjim','price','link'])
    df_done = df.sort_values(by=['jjim'], ascending=False)
    df_done['input_date'] = now
    print(df_done)
    df_done = df_done.reset_index(drop=True)

    result = db_conn.sql_insert(df_done)
    
    # 데이터프레임을 dict형식으로 변경코드
    # result_dict = df_done.to_dict('index')
    # result_num = len(result_dict)
    
        
    return print(result)


def all_categories():
    cat_list = []
    여성_신발 = 'https://search.shopping.naver.com/search/category?catId=50000173&frm=NVSHCAT&origQuery&pagingIndex=1&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list'

