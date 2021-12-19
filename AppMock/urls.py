"""AppMock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from Myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_list/',project_list),

    re_path('del_project/(?P<pid>.+)/',del_project), # 添加删除项目的url
    path('add_project/',add_project),
    path('save_project/',save_project), #保存项目
    path('',project_list), # 进入项目首页
    path('login/',login),
    path('sign_in/',sign_in),
    path('sign_up/',sign_up),
    path('accounts/login/',login),
    path('logout/',logout),
    path('reset_password/',reset_password),
    path('send_email_pwd/',send_email_pwd),
    path('project_data/',project_data), #获取项目所有数据


    re_path('mock_list/(?P<project_id>.+)/', mock_list),  # 进入项目详情页(mock列表页)
    re_path('add_mock/(?P<project_id>.+)/', add_mock),  # 新增单元
    re_path('del_mock/(?P<mock_id>.+)/', del_mock),  # 删除单元
    path('save_mock/',save_mock), #保存单元
    path('get_mock/',get_mock), #获取单元


]
