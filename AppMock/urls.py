from django.contrib import admin
from django.urls import path,re_path
from Myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_list/',project_list),
    re_path('del_project/(?P<pid>.+)/',del_project), # 添加删除项目的url
    path('add_project/',add_project),
    path('save_project/',save_project), #保存项目
    path('project_data/', project_data),  # 获取项目所有数据
    path('',project_list), # 进入项目首页

    path('login/',login),
    path('sign_in/',sign_in),
    path('sign_up/',sign_up),
    path('accounts/login/',login),
    path('logout/',logout),
    path('reset_password/',reset_password),
    path('send_email_pwd/',send_email_pwd),


    re_path('mock_list/(?P<project_id>.+)/', mock_list),  # 进入项目详情页(mock列表页)
    re_path('add_mock/(?P<project_id>.+)/', add_mock),  # 新增单元
    re_path('del_mock/(?P<mock_id>.+)/', del_mock),  # 删除单元
    path('save_mock/',save_mock), #保存单元
    path('get_mock/',get_mock), #获取单元
    re_path('mock_on/(?P<mock_id>.+)/',mock_on), #启用单元
    re_path('mock_off/(?P<mock_id>.+)/',mock_off),#禁用单元
    ##### 测试调试
    # path('demo_span/',demo_span), # 调试用接口
    re_path('server_on/(?P<project_id>.+)/', server_on),  # 启用服务
    re_path('server_off/(?P<project_id>.+)/', server_off),  # 禁用服务
    path('get_catch_log/',get_catch_log),
    path('import_catch/', import_catch),  # 导入服务
]
