#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过前端传入所要访问的页面
# python读取第一次扫描时存取的vulnurl.txt的文件
# 读取所需页面的所需条目
# 将读取到条目传入到apiroute引用的地方

import sys
import requests
import os
import numpy as np
import threading


class page_search_fun:
    path = os.getcwd()+'/scanner/plugins/filescan/vulnurl.txt'
    def __init__(self,page):
        self.page = page

    #写入文件
    def Datawrite(data):
        with open(page_search_fun.path,'w') as f:
            f.writelines(data)
            f.write('\n')
        
    #返回行数
    def Dataline():
        f = open(page_search_fun.path,'r')
        count = len(f.readlines())
        return count

    #读取文件
    def Dataread(pages):
        with open(page_search_fun.path,'r',encoding='utf-8',) as f:
            line=f.readlines()
            pages = int(pages)
        return line[(pages-1)*10:pages*10]

    #运行函数
    def run(self):
        try:
            count = page_search_fun.Dataline()/10
            results = page_search_fun.Dataread(self.page)
            return results,count
        except:
            err = "[-] ======>连接超时"
            return err,0

def start():
    testVuln = page_search_fun(sys.argv[1])
    testVuln.run()

if __name__ == "__main__":
    th=[]
    th_num=10
    for x in range(th_num):
        t=threading.Thread(target=start)
        th.append(t)
    for x in range(th_num):
        th[x].start()
    for x in range(th_num):
        th[x].join()