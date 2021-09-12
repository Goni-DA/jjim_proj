
# 셀레니움 패키지를 활용하여 필요한 정보를 수집 후 업로드 하기 위한 코드입니다.

# 웹 페이지에서 필요한 정보를 수집하는 함수 : jjim_file()
# 사용자가 검색어를 입력하면, 해당 검색어의 결과에 맞춘 url을 반환.
# 반환한 url을 기반으로 데이터를 수집하고(db 적재), 적재한 데이터에서 Top 5개를 불러옵니다.

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
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

options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

# 검색어를 입력하고, 자동으로 입력결과 페이지를 출력하는 함수
def return_url():
    ask = input()
    driver.get('https://shopping.naver.com/home/p/index.naver')
    
    # 검색어 입력
    xpath2 = "//input[@class='co_srh_input _input N=a:SNB.search']"  # //는 이전 경로들을 축약한 뜻
    driver.find_element_by_xpath(xpath2)
    driver.find_element_by_xpath(xpath2).clear()
    driver.find_element_by_xpath(xpath2).send_keys(ask)
    driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()
    driver.implicitly_wait(time_to_wait=2)
    current_url_ = driver.current_url
    
    return current_url_


# 현재 페이지에서 필요한 정보들을 받아보자
def jjim_file(url):
    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(4) # 무작정 기다리는게 아니라 조건 성립할때 까지만 기다리는 기능 추가 필요

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

    df = pd.DataFrame(list(zip(pn_list,jj_list, price_list, link_list)), columns = ['sham_name','jjim_num','price_list','link'])
    df_done = df.sort_values(by=['jjim_num'], ascending=False)
    df_done['add_date'] = now
    print('**** 데이터프레임 생성완료')
    # print용 변수
    data_num = len(df_done)

    print('**** 수집된 데이터는 {}개 입니다.'.format(data_num))
    df_done = df_done.reset_index(drop=True)

    result = db_conn.sql_insert(df_done)
    
    # 데이터프레임을 dict형식으로 변경코드
    # result_dict = df_done.to_dict('index')
    # result_num = len(result_dict)
    
        
    return print(result)


def all_categories():
    cat_list = []
    여성_신발 = 'https://search.shopping.naver.com/search/category?catId=50000173&frm=NVSHCAT&origQuery&pagingIndex=1&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list'

