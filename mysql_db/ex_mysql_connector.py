import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='781220', database='northwind_cn')

cursor = db.cursor()
search_word = input('请输入要查询的条件：')
cursor.execute(f'select * from product where productname like %s', (f'%{search_word}%',))
products = cursor.fetchall()
db.close()

for product in products:
    print(product)
