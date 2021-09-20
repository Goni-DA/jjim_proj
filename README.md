# jjim_proj

## 1.1 개요

네이버 쇼핑의 카테고리별 제품의 목록을 크롤링하여, 찜하기가 높은 순서대로 정렬할 수 있는 Web기반 서비스 개발 프로젝트입니다.

## 2.1 배경

웹 크롤링 기술을 바탕으로, 어떤 기능들을 구현할 수 있을까 고민하던 차에 네이버 쇼핑의 정렬방법에는 찜하기 순으로 정렬하는 Logic이 없는 것을 확인했습니다.
해당 Needs를 바탕으로 솔루션을 구성해 보았으며 1인 개발 서비스 입니다.

## 2.2 서비스 기능 위주 설명
사용자가 정렬 희망하는 사이트의 URL을 입력하면, 해당 사이트의 물품정보들을 크롤링 후 결과 페이지에 제품명, 찜하기 갯수, 상세페이지 URL을 제공하는 것이 목표입니다.

### 2.2.1 현재 구현 기능 (21.09.08)
* url 정보가 주어졌을 때 페이지 로딩 후 정보 크롤링 (Python / Selenium)
* 크롤링 된 정보를 엑셀 파일로 저장
* 랜덤 사용자가 접근할 수 있도록 URL 주소 접수 받을 수 있는 웹 Page (Flask)
* 가격 정보 추가수집 (컬럼추가) (21.08.30)
* Maria DB 설치(local) 및 table 생성 완료 (21.08.30)
* 수집한 데이터에 수집시점 컬럼 추가
* 수집완료 데이터(dataframe 형식)를 MariaDB로 적재 성공(일부 오류 잔재) (21.09.08)
* 가상 서버 호스팅 완료 / AWS 라이트세일, 도메인 주소 구매 후 네임서버 연결, 워드프레스 기반 기초 웹페이지 호스팅 성공 (21.09.15)


### 2.2.2 추가 구현 필요 기능
* 크롤링 위한 페이지 로딩 시 시간 지연 문제 개선 (현재는 sleep 기능으로 단순 지연)
* 시간단위 혹은 일단위 자동 크롤링 및 데이터 수집 후 My SQL 서버로의 저장 기능
* 웹 Page template 수정 
* 웹 호스팅 관련 학습 진행중 (cafe24 기초 도메인 활용하여 배포 예정)
* 웹 서버와 연계하여, 실제 서비스를 제공할 수 있도록 웹 페이지 배포 필요 (Docker 공부중이지만.. 미흡)
* 각 카테고리별 찜하기 상위 5개 시각화 할 수 있으면 좋을 것으로 판단.


## 2.3 데이터 분석
### 2.3.1 분석의 방향성 (still Developing)
* 일단위 수집된 데이터를 활용하여 카테고리별 찜하기 갯수의 변동 현황을 분석, 변동현황을 활성화지수로 명명하고 활성화지수에 따른 주가변화(상관관계 확인 혹은 예측) 등 기업활동변화와의 연계성 확인


## 2.4 시각화
### 2.4.1 차트 종류
* 찜하기 개수의 변동폭이 큰 제품을 확인할 수 있는 그래프
* 찜하기 상위 5개 씩 나와있는 테이블(반응형)
