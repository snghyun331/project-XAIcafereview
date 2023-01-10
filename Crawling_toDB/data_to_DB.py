import pymysql
import pandas as pd

df = pd.read_csv('origin_data.csv',encoding='utf8',index_col=0)

connect = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "sng24678@",
    database='cafe_reviewDB'
)
cursor = connect.cursor()

sql = "insert into reviews VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
for idx in range(len(df)):
    cursor.execute(sql, tuple(df.values[idx]))
    
connect.commit()  # 결과 저장


# 테이블 안의 데이터 확인
query = "Select * from 전체리뷰들"
sample = pd.read_sql(query, connect)
#print(sample.shape)
print(sample)


connect.close()