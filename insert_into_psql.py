
# 插入一百万条数据
import random
from faker import Faker
import psycopg2
f = Faker('zh_CN')

conn = psycopg2.connect("dbname=mytest user=gongyan")
cur = conn.cursor()
num = iter(range(2000000))
def gender():
    return random.choice([0,0,0,0,1,1,1,1,1,2])

while True:
    try:
        next(num)
    except Exception as e:
        break
    else:
        name,age,month,birthday,province,job = f.name(),random.randint(1,80),f.month_name(),f.date(pattern="%Y-%m-%d", end_datetime=None),f.province(),f.job()
        print(name,age,gender,month,birthday,province,job)
        cur.execute("INSERT INTO info VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,age,gender(),month,birthday,province,job[:20]))
        conn.commit()
        print('提交成功')