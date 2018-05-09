#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import string
import zipfile
import optparse
import itertools as its
from threading import Thread



def welcome():
    print ('welcome to zipfile attack py')
    time.sleep(1)


def attack (zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] found password'+password+'\n'
    except:
        pass

def dicProduce():
    choose=raw_input('input y/n to produce a new dictionary or not')
    try:
        if choose=='y':
            print('please make sure that high>low and both >0')
            low=int(raw_input('please input the digit(low)'))
            high=int(raw_input('please input the digit(high)'))
            high=high+1
            words1=string.lowercase
            words2=string.uppercase
            words3=string.letters
            words4=string.printable
            with open('pass.txt','w')as dic:
                print ('dictionary mode\n')
                print('1 pure digital\n')
                print('2 pure lowercase letters\n')
                print('3 pure uppercase letters\n')
                print('4 pure letters\n')
                print('5 printable\n')
                print('6 custom\n')

                choose1=raw_input('please choose a dictionary mode')
                if choose1=='1':
                    for temp in range(high):
                        d=-1
                        if temp>=low:
                            for i in range(pow(10,temp)):
                                d=int(d)
                                d=d+1
                                d=str(d)
                                s=d.zfill(temp)
                                dic.write(s+'\n')
    
                elif choose1=='2':
                    for temp in range(high):
                        if(temp>=low):
                            prl = its.product(words1, repeat=temp)
                            for i in prl:
                                dic.write("".join(i))
                                dic.write("".join("\n"))
                elif choose1=='3':
                    for temp in range(high):
                        if(temp>=low):
                            pul = its.product(words2, repeat=temp)
                            for i in pul:
                                dic.write("".join(i))
                                dic.write("".join("\n"))
                elif choose1=='4':
                    for temp in range(high):
                        if (temp >= low):
                            prl = its.product(words3, repeat=temp)
                            for i in pl:
                                dic.write("".join(i))
                                dic.write("".join("\n"))
                elif choose1 == '5':
                    for temp in range(high):
                        if(temp>=low):
                            pa = its.product(words4, repeat=temp)
                            for i in pa:
                                dic.write("".join(i))
                                dic.write("".join("\n"))
                elif choose1 == '6':
                    words5=raw_input("please input your character\n")
                    for temp in range(high):
                        if(temp>=low):
                            ct = its.product(words5, repeat=temp)
                            for i in ct:
                                dic.write("".join(i))
                                dic.write("".join("\n"))
            dic.close()
        else:
            pass
    except:
        pass



def main():
    welcome()

    parser=optparse.OptionParser("usage%prog "+\
    "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', \
    help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', \
    help='specify dictionary file')
    (options, args)=parser.parse_args()

    dicProduce()

    if(options.zname==None) | (options.dname==None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    print zname
    print dname
    passfile = open(dname)
    for line in passfile.readlines():
        password = line.strip('\n')
        # attack(zFile, password)
        t = Thread(target=attack, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
