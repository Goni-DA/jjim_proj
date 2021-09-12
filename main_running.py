import web_open as wo
import legacy_code.web_open as lwo
import sql_code.pd_sql_direct_conn as db_conn


#url = 'https://search.shopping.naver.com/search/all?query=%EC%B9%B4%EB%93%9C%EC%A7%80%EA%B0%91&frm=NVSHATC&prevQuery=%EC%83%B4%ED%91%B8'

url = wo.return_url()
wo.jjim_file(url)
db_conn.sql_select()
