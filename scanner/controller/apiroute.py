from ..app import json,requests,request,make_response,socket,jsonify,Blueprint,plugins
import re

# 用蓝图注册路由
api = Blueprint('api', __name__)

def getjson():
    return json.loads(request.get_data().decode("utf-8"))

#文件扫描 /plugins/filescan/folder_scan_fun.py
@api.route('/filescan', methods=['post'])
def filescan_api():
    # 获取前端传入的json数据
    filescan_load = getjson()
    url = filescan_load['url']
    utype = filescan_load['type']
    page = filescan_load['page']
    # 引用算法，算法返回数据
    (filescan_poc_result,filescan_poc_page) = list(plugins.angelsword['filescandict'].values())[utype](url,page).run()
    # 处理数据，返回前端
    filescan_poc_url=[]
    filescan_poc_status = []
    for result in filescan_poc_result:
        filescan_poc_url+=re.findall(r"](.+?)$",result)
        if "[200" in result:
            filescan_poc_status.append('200')
        elif "[301" in result:
            filescan_poc_status.append('301')
    return jsonify({"status": filescan_poc_status,"url":filescan_poc_url,"page":filescan_poc_page})


#页数 /plugins/filescan/page_search_fun.py
@api.route('/page', methods=['post'])
def page_api():
    # 获取前端传入的json数据
    filescan_load = getjson()
    filescan_page = filescan_load['page']
    filescan_type = filescan_load['type']
    # 引用算法，算法返回数据
    (filescan_poc_result,filescan_poc_page) = list(plugins.angelsword['filescandict'].values())[filescan_type](filescan_page).run()
    # 处理数据，返回前端
    filescan_poc_url=[]
    filescan_poc_status = []
    for result in filescan_poc_result:
        filescan_poc_url+=re.findall(r"](.+?)$",result)
        if "[200" in result:
            filescan_poc_status.append('200')
        elif "[301" in result:
            filescan_poc_status.append('301')
    return jsonify({"status": filescan_poc_status,"url":filescan_poc_url,"page":filescan_poc_page})




# cms漏洞利用 /plugins/CompileCMS
@api.route('/CompileCMS', methods=['post'])
def cms_api():
    # 获取前端传入的json数据
    cmsexp_load = getjson()
    cmsexp_url = cmsexp_load['url']
    cmsexp_type = cmsexp_load['type']
    # 引用算法，算法返回数据
    cmsexp_poc_result = list(plugins.angelsword['compileCMSdict'].values())[cmsexp_type](cmsexp_url).run()
    # 处理数据，返回前端
    if cmsexp_poc_result is not None:
        if "[+]" in cmsexp_poc_result:
            cmsexp_poc_status = 1
        else:
            cmsexp_poc_status = 0
    else:
        cmsexp_poc_result = "[-]no vuln"
        cmsexp_poc_status = 0
    return jsonify({"status": cmsexp_poc_status, "pocresult": cmsexp_poc_result})

#弱口令扫描 /plugins/weakScan
@api.route('/Weakscan', methods=['post'])
def WeakScan_api():
    # 获取前端传入的json数据
    Weakscan_load = getjson()
    Weakscan_url = Weakscan_load['url']
    Weakscan_param = Weakscan_load['param']
    Weakscan_tag = Weakscan_load['tags']
    Weakscan_type = Weakscan_load['type']
    # 引用算法，算法返回数据
    Weakscan_poc_result = list(plugins.angelsword['WeakScandict'].values())[Weakscan_type](Weakscan_url,Weakscan_param,Weakscan_tag).run()
    # 处理数据，返回前端
    Weakscan_poc_status=0
    result=''
    if Weakscan_poc_result is not None:
        if "[success]" in Weakscan_poc_result:
            Weakscan_poc_status = 1
            result = re.findall(r"](.+?)$",Weakscan_poc_result)
        elif "[failed]" in Weakscan_poc_result:
            Weakscan_poc_status = 0
            result = '未扫描到用户名'
        elif "[down]" in Weakscan_poc_result:
            Weakscan_poc_status = 2
            result = 'ftp服务未开启'
    else:
        result = "[-]no vuln"
        Weakscan_poc_status = 3
    return jsonify({"status":Weakscan_poc_status, "pocresult":result})