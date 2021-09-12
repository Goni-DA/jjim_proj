import pandas as pd
import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


import pandas as pd


db_connection_str = "mysql+pymysql://{user}:{pw}@127.0.0.1/{db}".format(user='root', pw='maria1234', db='jjim_prj_db')
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()

def sql_insert (dataframe):
    df = pd.DataFrame(data=dataframe, columns=['sham_name','jjim_num','price_list','link','add_date'])
    
    dtypesql = {'sham_name':sqlalchemy.types.VARCHAR(200), 
          'jjim_num':sqlalchemy.INT(), 
          'price_list':sqlalchemy.types.VARCHAR(50), 
          'link':sqlalchemy.types.VARCHAR(5000), 
          'add_date':sqlalchemy.types.VARCHAR(30) 
        }

    df.to_sql(name='pd_shampoo', con=db_connection, if_exists='append',index=False, dtype=dtypesql)  

    
    cnt_done = len(df) 
    result = '**** SQL문 삽입결과  :{}건 삽입되었습니다.'.format(cnt_done)
    return result


conn2 = pymysql.connect(
        user="root",
        password="maria1234",
        host="127.0.0.1",
        port=3306,
        database="jjim_prj_db"
    )

def sql_select():
    cur = conn2.cursor()
    cur.execute('select * from pd_shampoo')
    res = cur.fetchall()
    data = pd.DataFrame.from_records(res)
    print(data)
    return data







# #마리아 DB 라이브러리 활용하여 DataFrame 형태 자체를 import 하는 방법 Seeking중
# conn  = pymysql.connect(
#     user='root', 
#     password='maria1234', 
#     database='jjim_prj_db', 
#     host='127.0.0.1',
#     port=3306
# )


# def sql_insert (dataframe):
#     df = pd.DataFrame(data=dataframe, columns=['sham_name','jjim_num','price_list','link','add_date'])
#     df.to_sql(name='db의 테이블이름', con=db_connection, if_exists='append',index=False)  

#     engine = create_engine("mysql://{user}:{pw}@127.0.0.1/{db}".format(user='root', pw='maria1234', db='jjim_prj_db'))
    
#     df = pd.DataFrame(data=dataframe, columns=['sham_name','jjim_num','price_list','link','add_date'])
#     print(df)
#     df[pd.isnull(df)] = None
#     data = list(df.itertuples(index=False, name=None))
#     print(data)
#     data[0]

#     sql = """
#     INSERT INTO pd_shampoo (
#         sham_name,
#         jjim_num,
#         price_list,
#         link,
#         add_date
#     ) VALUES (
#         ?, ?, ?,
#         ?, ?
#     )
#     """

#     cs = conn.cursor()
#     cs.executemany(sql, data)
#     conn.commit()


#     cnt_done = 1 #'총 insert 완료된 data 행의 갯수 계산 하는 코드'     
#     # result = 'SQL문 삽입결과  :{}건 삽입되었습니다.'.format(cnt_done)
#     return print(cnt_done)

