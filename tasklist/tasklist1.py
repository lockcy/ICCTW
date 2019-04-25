#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @auther : lockcy
import os
import re
import time
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码

def get_tasklist():
    data=os.popen('tasklist /nh' ,'r')
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    flag=1
    while True:
        i=data.readline()
        if i.strip()=='':
            if flag==1:
                flag=0
                continue
            else:
                break
        #pname = re.findall('^\w+', i)[0]
        pname=i.split('  ')[0].strip()
        pid = re.findall('\d+', i)[0]
        ptype = re.findall('Services|Console', i)[0]
        pmemory = re.findall('[\w+,]*\w* K$', i)[0][:-2].replace(',','')
        if int(pmemory,10)<100000:
            continue
        p1.append(pname)
        p2.append(pid)
        p3.append(ptype)
        p4.append(pmemory)
        print('pname->'+pname+' pid->'+pid+'+ptype->'+ptype+'+pmemory->'+pmemory)


    plt.figure(figsize=(10, 9))  # 调节图形大小
    labels = p1  # 定义标签
    sizes = p4  # 每块值
    colors = ['yellow', 'red', 'blue','green']
    patches, text1, text2 = plt.pie(sizes,
                                    labels=labels,
                                    colors=colors,
                                    autopct='%3.2f%%',  # 数值保留固定小数位
                                    shadow=False,  # 无阴影设置
                                    startangle=90,  # 逆时针起始角度设置
                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
    # patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    time1=get_time()
    plt.title(time1,fontsize='large')
    plt.show()



def get_time():
    time_now=time.strftime('%H:%M',time.localtime(time.time()))
    #print ('time now->'+time_now)
    return time_now


if __name__=='__main__':
    #get_time()
    get_tasklist()
