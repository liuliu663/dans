#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过前端传入URL,已知参数，和扫描所需结果
# python 模拟 登录ftp，通过成功和失败来判断用户名或密码是否成功
# 成功则返回，未成功则继续

import sys
import requests
import os
import ftplib
import socket


class Weak_FTP_Scan:
    def __init__(self,url,param,tags):
        self.url = url
        self.param = param
        self.tags = tags

    #读文件
    def Dataread(path):
        with open(path,'r',encoding='utf-8') as f:
            line=f.readlines()
        return line

    #确认端口是否开启
    def PortConfirm(url,port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sk.connect((url,21))
            return 1
        except Exception:
            sk.close()
            return 0

    #已知密码，爆破用户
    def login_USER(url,param):
        path = os.getcwd()+'/scanner/plugins/weakScan/dic/user.txt'
        line = Weak_FTP_Scan.Dataread(path)[1:]
        for uname in line:   
            user = uname.rstrip()
            try:
                ftp = ftplib.FTP()
                ftp.connect(url,21,0.05)
                ftp.login(user,param)
                ftp.quit()
                return user
            except:
                pass
        return 'failed'

    #已知用户，爆破密码
    def login_PASS(url,param):
        path = os.getcwd()+'/scanner/plugins/weakScan/dic/pass.txt'
        line = Weak_FTP_Scan.Dataread(path)[1:]
        for password in line:   
            pwd = password.rstrip()
            try:
                ftp = ftplib.FTP()
                ftp.connect(url,21,0.05)
                ftp.login(param,pwd)
                k=ftp.getwelcome()
                ftp.quit()
                return pwd
            except:
                pass
        return 'failed'

    #运行函数
    def run(self):
        port = 21
        if (Weak_FTP_Scan.PortConfirm(self.url,port)):
            try:#分类运行爆破方式
                if 'USER' in self.tags:
                    data = Weak_FTP_Scan.login_USER(self.url,self.param)
                    if 'failed' in data:
                        return ['failed']
                elif 'PASS' in self.tags:
                    data = Weak_FTP_Scan.login_PASS(self.url,self.param)
                    if 'failed' in data:
                        return ['failed']
                return '[success]'+data
            except:
                return '[-] no vuln'
        else:
            return '[down]'


if __name__ == "__main__":
    testVuln = Weak_FTP_Scan(sys.argv[1])
    testVuln.run()