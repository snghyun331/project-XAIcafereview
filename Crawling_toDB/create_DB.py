import pymysql
import pandas as pd
# pd.set_option('display.max_columns',None)

####### MySql내 cafe_reviewDB 생성 #######
connect = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "sng24678@"
)

cursor = connect.cursor()

# Database 생성구문
cursor.execute("CREATE DATABASE cafe_reviewDB")
connect.commit()  # 결과 저장

# DB목록 확인
cursor.execute("SHOW DATABASES")
for data in cursor:
    print(data)
    
######## cafe_reviewDB내 review 테이블 생성 #########

import pymysql
import pandas as pd

connect = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "sng24678@",
    database='cafe_reviewDB'
)
cursor = connect.cursor()

#'reviews' 테이블 및 컬럼 생성
sql = """CREATE TABLE reviews (region char(10), cafe_name longtext, average_star float default 0,
        load_user_id longtext, review_date varchar(20), each_star float default 0,
        review_text longtext, label int)
        """
cursor.execute(sql)
connect.commit()  # 결과 저장

#TABLE 목록 확인
cursor.execute("SHOW TABLES")
for data in cursor:
    print(data)
    
#Table 안의 컬럼 정보 확인
cursor.execute("desc reviews")
for data in cursor:
    print(data)
    
