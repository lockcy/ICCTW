#!/usr/bin/python
#-*- coding:utf-8 -*-

import random
import xlrd

ExcelFile = xlrd.open_workbook(r'test1.xlsx')
sheet = ExcelFile.sheet_by_name('Sheet1')
i = []
x = input("请输入具体事件：")
y = int(input("老师要求的字数："))
z= input('输入老师姓： ')
while len(str(i)) < y * 1.2:
    s = random.randint(0,3)
    rows = sheet.row_values(s)
    i.append(*rows)
print(" "*8+"检讨书"+"\n"+str(z)+"老师：")
print("我不应该" + str(x)+"，", i)
print("再次请老师原谅！")

