#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过前端传入URL,已知参数，和扫描所需结果
# python 模拟 登录ssh，通过成功和失败来判断用户名或密码是否成功
# 成功则返回，未成功则继续

import threading
import sys
import requests
import os
import socket
from pexpect import pxssh
import grequests
import paramiko
import time


class Weak_SSH_Scan:
    def __init__(self,url,param,tags):
        self.url = url
        self.param = param
        self.tags = tags

    #文件读取
    def Dataread(path):
        with open(path,'r',encoding='utf-8') as f:
            line=f.readlines()
        return line

    #确认端口是否开启
    def PortConfirm(url):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sk.connect((url,22))
            return 1
        except Exception:
            sk.close()
            return 0

    #已知密码，爆破用户
    def login_USER(url,param):
        path = os.getcwd()+'/scanner/plugins/weakScan/dic/user.txt'
        line = Weak_SSH_Scan.Dataread(path)[1:]
        for uname in line:   
            user = uname.rstrip()
            try:
                ssh=paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=url,username=user,password=param,timeout=1)
                ssh.close()
                print ('[+] SSH weak password:'+user+','+param)
                return user
            except:
                pass
        return 'failed'

    #已知用户，爆破密码
    def login_PASS(url,param):
        path = os.getcwd()+'/scanner/plugins/weakScan/dic/pass.txt'
        line = Weak_SSH_Scan.Dataread(path)[1:]
        for password in line:
            pwd = password.rstrip()
            try:
                ssh=paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=url,username=param,password=pwd,timeout=1)
                return pwd
            except:
                pass
        return 'failed'

    #主函数
    def run(self):
        if (Weak_SSH_Scan.PortConfirm(self.url)):
            # try:#分类运行爆破方式
            if 'USER' in self.tags:
                print('user')
                data=Weak_SSH_Scan.login_USER(self.url,self.param)
                if 'failed' in data:
                    return ['failed']
            elif 'PASS' in self.tags:
                print('pass')
                data=Weak_SSH_Scan.login_PASS(self.url,self.param)
                if 'failed' in data:
                    return ['failed']
            return '[success]'+data
            # except:
            #     return '[-] no vuln'
        else:
            return '[down]'

def start():
    testVuln = Weak_SSH_Scan(sys.argv[1])
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