import pymysql

conn = None
cur = None

sql =""

# 마리아 DB 와의 연결 성공
conn = pymysql.connect(host="127.0.0.1", user="root", password="maria1234", db='jjim_prj_db')
cur = conn.cursor()

#간단한 조회문
sql = "SELECT * FROM pd_shampoo;"
cur.execute(sql)


# SQL insert 입력날짜 값을 추가하는 SQL문
# Maria db에서는 curdate() 가 오늘날짜 출력함.



# 완료한 데이터를 받음.
rs = [cur.fetchall()]
print(rs)

conn.commit()
conn.close()

# 데이터 베이스와 python을 Dataframe 형태로 직접 입력할 수 있음.
# 나중에라도 참고해 봅시다.
# https://youngwonhan-family.tistory.com/48

