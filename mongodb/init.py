import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['northwind']

client.drop_database(db)

collection_products = db['products']
collection_categories = db['categories']
collection_suppliers = db['suppliers']

with open('northwind.json','rb') as f:
    products = json.loads(f.read(), encoding='utf-8')

suppliers = [dict(SupplierId=item[0], SupplierName=item[1]) for item in {(p['SupplierId'],p['SupplierName']) for p in products}]
categories = [dict(CategoryId=item[0], CategoryName=item[1]) for item in {(p['CategoryId'],p['CategoryName']) for p in products}]

sorted(products, key=lambda p: p['ProductId'])
sorted(categories, key=lambda c: c['CategoryId'])
sorted(suppliers, key=lambda s: s['SupplierId'])

collection_products.insert_many(products)
collection_categories.insert_many(categories)
collection_suppliers.insert_many(suppliers)
