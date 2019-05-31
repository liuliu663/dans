# onlinetools

这是一款线上网站评级系统，并根据相关扫描功能收集整理了一些渗透测试过程中常见的需求
现在已经包含的功能有：
在线cms识别|poc漏洞检测|文件后台扫描|端口功能判断|网站扫描管理|网站评级功能

# 部署方法

    cd onlinetools
    pip3 install -r requirements.txt
    nohup python3 main.py &

浏览器打开
    http://localhost:8000/

# 说明
1.poc漏洞检测：
    a. 注册路由CompileCMS
    b. 显示页面CompileCMS.html
    c. 算法目录/scanners/plugins/CompileCMS
    d. 每个算法将漏洞模拟一次，并返回数据
2.CMS使用在线api
3.文件后台扫描：
    a. 注册路由filescan
    b. 显示页面filescan.html
    c. 算法目录/scanners/plugins/filescan
    d. 算法模拟访问目录。
4.端口功能判断：
    a. 注册路由weakscan
    b. 显示页面WeakScan.html
    c. 算法目录/scanners/plugins/weakScan
    d. 算法模拟登录SSH及FTP
5.网站扫描管理
6.网站评级功能
7.本工具仅限于进行漏洞验证，如若因此引起相关法律问题，概不负责。





