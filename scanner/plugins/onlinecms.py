#coding=utf-8
import requests
import json
import time
import re
import sys
# 这个是用了一个在线的onlinecms

class gonlineweb:
    def __init__(self,url):
        self.url = url
        self.time=0

    def onlineweb(self):
        url = 'http://whatweb.bugscaner.com/what.go/'
        start = time.clock()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0','Referer':'http://whatweb.bugscaner.com/look/'}
        cocokies = {'saeut': 'CkMPHlqbqdBQWl9NBG+uAg=='}
        new_url = self.url.strip('/').replace('http://','').replace('https://','')
        data = {'url': new_url}
        content = requests.post(url,headers=headers,data=data, timeout=30).json()
        end = time.clock()
        self.time = end - start
        if content['CMS']:
            result = "CMS: "+str(content['CMS'])#+",Web Servers: "+str(content['Web Servers'][0])
            try:
                return {
                    "total":1424,
                    "url":self.url,
                    "result":result,
                    "time":"%.3f s" % self.time
                }
            except:
                return  {
                    "total":1424,
                    "url":self.url,
                    "result":content['CMS'],
                    "time":"%.3f s" % self.time
                }
        else:
            return  {
                "total":1424,
                "url":self.url,
                "result":"未知CMS",
                "time":"%.3f s" % self.time
            }
       
if __name__ == "__main__":
    testVuln = gonlineweb(sys.argv[0])
    testVuln.onlineweb()
