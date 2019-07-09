#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""mongodb_demo.py"""

import pymongo
from bson.objectid import ObjectId

conn = pymongo.MongoClient('localhost', 27017)  # 连接

db_school = conn.school  # 数据库

# 集合
col_students = db_school.students
col_teachers = db_school.teachers
col_courses = db_school.courses

for c in col_courses.find().limit(3): print(c)

conn.close()  # 关闭数据库
