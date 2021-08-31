import pandas as pd
import pymysql
from sqlalchemy import create_engine


#마리아 DB 라이브러리 활용하여 DataFrame 형태 자체를 import 하는 방법 Seeking중
conn  = pymysql.connect(
    user='root', 
    password='maria1234', 
    database='jjim_prj_db', 
    host='127.0.0.1',
    port=3306
)

# 위 커넥션 정보와 동일하게 입력
engine = create_engine("mysql://{user}:{pw}@127.0.0.1/{db}".format(user='root', pw='maria1234', db='jjim_prj_db'))

dummy_data = [2, 'namedum', 3, 'real_fake', '2021-08-31']
df = pd.DataFrame(data=dummy_data, columns=['pno','jjim_name','jjim_num','link_name','add_date'])
print(df)
data = list(df.itertuples(index=False, name=None))
print(data)
data[0]

sql = """
INSERT INTO pd_shampoo (
    pno,
    sham_name,
    jjim_num,
    link,
    add_date
) VALUES (
    ?, ?, ?,
    ?, ?
)
"""

cs = conn.cursor()
cs.executemany(sql, data)
conn.commit()