import pymysql

db = pymysql.connect('localhost', 'root', '781220', 'northwind_cn')
cursor = db.cursor()

search_word = input('请输入要查询的条件：')
cursor.execute('select * from product where productname like %s', (f'%{search_word}%',))
products = cursor.fetchall()
db.close()

for product in products:
    print(product)
