from ..app import app,render_template,request,re,Markup,plugins,session
from ..plugins.onlinecms import gonlineweb
from ..orm import db_session
from ..model.user import User
import json

#在使用蓝图之前，通过@app.route注册
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/JudgeRank',methods=['get','post'])
def JudgeRank():


#路由
@app.route('/onlineCMS', methods=['get', 'post'])
def onlinecms():
    if request.method == 'POST':
        url = request.form.get("url")
        if re.match(r'^https?:/{2}\w.+$', url):
            try:
                onlinecmsresult = gonlineweb(url).onlineweb()
                print(onlinecmsresult)
                return render_template('onlineCMS.html', data=onlinecmsresult, title='CMS识别')
            except:
                onlinecmsresult = {'total': '', 'url': '', 'result': '', 'time': ''}
                return render_template('onlineCMS.html', data=onlinecmsresult, title='CMS识别')
    elif request.method == 'GET':
        return render_template('onlineCMS.html', title="CMS识别")

@app.route('/filescan')
def file_scan():
    return render_template('filescan.html', title='文件扫描', data=Markup(list(plugins.angelsword['filescandict'].keys())))


@app.route('/CompileCMS')
def cms_scan():
    return render_template('CompileCMS.html', title='cms安全检测', data=Markup(list(plugins.angelsword['compileCMSdict'].keys())))

@app.route('/Weakscan')
def Weak_scan():
    return render_template('WeakScan.html', title='弱口令扫描', data=Markup(list(plugins.angelsword['WeakScandict'].keys())))


# 会话控制
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()