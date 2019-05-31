#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过前端传入URL,页面(扫描默认返回第一页)
# python 模拟request来返回status值，通过status判断所访问页面是否可访问
# 返回200和301,写在vulnurl.txt文件中
# 其他视为不可访问
# 将前十条传入到apiroute引用的地方

import sys
import requests
import os


class folder_scan_fun:
    #数据文件
    path = os.getcwd()+'/scanner/plugins/filescan/vulnurl.txt'
    def __init__(self,url,page):
        self.url = url
        self.page = page

    #文件写入
    def Datawrite(data):
        with open(folder_scan_fun.path,'w') as f:
            f.writelines(data)
            f.write('\n')
   
    #读行数
    def Dataline():
        f = open(folder_scan_fun.path,'r')
        count = len(f.readlines())
        return count

    #读取文件
    def Dataread(page):
        with open(folder_scan_fun.path,'r',encoding='utf-8') as f:
            line=f.readlines()
            page = int(page)
        return line[(page-1)*10:page*10]

    #运行函数
    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        result = []
        path = os.getcwd()+'/scanner/plugins/filescan/hh'
        files= os.listdir(path)
        for file in files: 
            paths=path+"/"+file
            vulnurl = []
            with open(paths,'rb') as f:
                for line in f.readlines():
                    if 'http://' in self.url:#判断用户输入是否存在http
                        vulnurl.append(self.url + line.decode(encoding='utf-8'))
                    else:
                        vulnurl.append('http://'+ self.url + line.decode(encoding='utf-8'))
        f.close()
        try:
            try:
                for url_v in vulnurl:#循环访问，并返回数据
                    url_v = url_v.replace('\r\n','')
                    req = requests.get(url=url_v, headers=headers, timeout=3, verify=False)
                    if req.status_code==200:
                        print(result)
                        result.append("[200:]"+url_v+'\r\n')
                    elif req.status_code==301:
                        result.append( "[301:]"+url_v+'\r\n')
            except :
                folder_scan_fun.Datawrite(result)
                count = folder_scan_fun.Dataline()/10
                results = folder_scan_fun.Dataread(self.page)
                return results,count
        except:
            err = "[-] ======>连接超时"
            return err,0

if __name__ == "__main__":
    testVuln = folder_scan_fun(sys.argv[1])
    testVuln.run()