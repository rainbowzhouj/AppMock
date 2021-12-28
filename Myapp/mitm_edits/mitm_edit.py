# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 3:42 下午
# @Author  : rainbowzhouj
# @FileName: mitm_edit.py
# @Software: PyCharm

from mitmproxy import http
import json
# 外部文件链接到orm
import django
import os, sys

sys.path.append('/Users/zhoujing/PycharmProjects/AppMock')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","AppMock.settings")
django.setup()
from Myapp.models import *


def request(flow):
    ...
    # 在发送请求前篡改发送的请求，编写干预的脚本，欺骗服务器
    # print("路过的url为：" + flow.request.url)
    # #修改请求  url 是字符串
    # if 'mock_list' in flow.request.url:
    #     old = flow.request.url
    #     flow.request.url = old.replace('20', '55')
    # 修改请求头  header，类型为字典，键值对
    # if 'mock_list' in flow.request.url:
    #     old = flow.request.headers
    #     old.update({"ccc": "ddd"})
    #
    # # # 拦截,可定义返回值 response为字典
    # if 'demo' in flow.request.url:
    #     flow.response = http.Response.make(200, "jjj", {"aaa": "bbb"})


def response(flow):
    project_id = os.path.basename(__file__).split('_')[0]

    mocks = DB_mock.objects.filter(project_id=project_id, state=True)
    # 在发送请求后篡改返回的响应，编写干预的脚本，欺骗服务器
    # # 实现 rewrite
    # if 'get_mock' in flow.request.url: # 此处为请求request 而不是response
    #     old=flow.response.text
    #     old=json.loads(old)
    #     print(old)
    #     old['mock']['name']='11111'
    #     flow.response.text=json.dumps(old)
    for m in mocks:
        # mitmproxy  如何通过orm访问数据库替换数据
        if m.catch_url in flow.request.url:
            all_updates = m.mock_response_body.split('\n')
            for u in all_updates:
                if '=>' in u:  # 普通替换规则
                    flow.response.text = flow.response.text.replace(u.split("=>")[0].rstrip(),
                                                                    u.split("=>")[1].lstrip())
                elif '=' in u:  # json 路径替换规则
                    try:
                        new = json.loads(flow.request.text)
                    except:
                        continue

                    key = u.split('=')[0].rstrip()  # rstrip() 函数作用：去除右边空格
                    value = eval(u.split('=')[1].lstrip())  # eval() 函数作用：能把字符串转化成python的各种数据类型
                    tmp_cmd = ''
                    for i in key.split('.'):
                        try:
                            int(i)
                            tmp_cmd += "[%s]" % i
                        except:
                            tmp_cmd += "[%s]" % repr(i)  # repr() 函数作用：去除右边空格

                    end_cmd = 'new' + tmp_cmd + "=value"
                    try:
                        exec(end_cmd)
                    except:
                        continue
                    flow.response.text = json.dumps(new)
                else:  # 不符合规则
                    ...
