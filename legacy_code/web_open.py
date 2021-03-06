
#url이 주어졌을 때 네이버 쇼핑에서 정보를 크롤링해와서 엑셀파일로 저장하는 코드



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
    time.sleep(4)

    pn_list = []
    jj_list = []
    link_list = []

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


    # 데이터를 데이터프레임으로
    df = pd.DataFrame(list(zip(pn_list,jj_list,link_list)), columns = ['Name','jjim','link'])
    df_done = df.sort_values(by=['jjim'], ascending=False)
    df_done = df_done.reset_index(drop=True)
    result_dict = df_done.to_dict('index')
    result_num = len(result_dict)

    #파일명에 현재시간 부여
    mask = '%m%d%Y'
    now = datetime.datetime.now().strftime(mask)
    fname = 'crw_file_{}.xlsx'.format(now)
    df_done.to_excel(fname)
    
        
    return result_dict, result_num




