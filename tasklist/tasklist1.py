#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @auther : lockcy
import os
import re
import time
from matplotlib import pyplot as plt
from collections import OrderedDict
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
system_call=['System Idle Process','System','Regisrty','wininit.exe','svchost.exe','fontdrvhost.exe','services.exe','smss.exe'\
             +'lsass.exe']
example=['KuGou.exe','SearchUI.exe','QQ.exe','explorer.exe','pycharm64.exe']
def get_tasklist():
    data=os.popen('tasklist /nh' ,'r')
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    flag=1
    others=0
    system=0
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
        if int(pmemory,10)<60000:
            others=others+int(pmemory,10)
            if pname in system_call:
                system=system+int(pmemory,10)
            continue
        p1.append(pname)
        p2.append(pid)
        p3.append(ptype)
        p4.append(pmemory)
        print('pname->'+pname+' pid->'+pid+'+ptype->'+ptype+'+pmemory->'+pmemory)
    p1.append('others')
    p4.append(others)
    p1.append('system')
    p4.append(system)

    painter_pie(p1,p4)


def painter_pie(data1,data2):
    plt.figure(figsize=(10, 9))  # 调节图形大小
    labels = data1  # 定义标签
    sizes = data2  # 每块值
    colors = ['yellow', 'red', 'blue', 'green', 'orange']
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
    time1 = get_time()
    plt.title(time1, fontsize='large')
    plt.show()

def painter_line(data1,time1,memory):
    fig=plt.figure(figsize=(10,10))
    #colors=['red','blue','green','black','orange']
    for i in range(len(data1)):
        plt.plot(time1,memory[i],label=data1[i])


    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.title('test')
    plt.xlabel('time')
    plt.ylabel('memory')
    plt.show()


def get_time():
    time_now=time.strftime('%H:%M',time.localtime(time.time()))
    #print ('time now->'+time_now)
    return time_now




if __name__=='__main__':
    #get_time()
    #get_tasklist()
    #time1=[1,2],[3,4],[5,6],[7,8]
    #memory=[2,3],[4,5],[6,7],[8,9]
    #painter_line(data1=example,time1=time1,memory=memory)

