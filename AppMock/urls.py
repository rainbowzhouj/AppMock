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
    path('',project_list), # 进入项目首页
    path('login/',login),
    path('sign_in/',sign_in),
    path('sign_up/',sign_up),
    path('accounts/login/',login),
    path('logout/',logout),
    path('reset_password/',reset_password),
    path('send_email_pwd/',send_email_pwd),

]
