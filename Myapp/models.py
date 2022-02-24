from django.db import models

# Create your models here.
class DB_project(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    creator=models.CharField(max_length=30,null=True,blank=True)
    run_counts=models.IntegerField(default=0)
    mocks_counts=models.IntegerField(default=0)
    state=models.BooleanField(default= False) #服务状态
    catch_log=models.TextField(default='[]')
    catch=models.BooleanField(default=False)# 抓日志的开关
    black_hosts=models.CharField(max_length=500,null=True,blank=True,default='')# 黑名单
    white_hosts=models.CharField(max_length=500,null=True,blank=True,default='')# 白名单，只抓白名单的东西
    catch_time=models.CharField(max_length=20,null=True,blank=True,default='')#最后一次获取抓包时间戳
    def __str__(self):
        return '项目名字是'+self.name




class DB_mock(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    state=models.BooleanField(default=False)
    project_id=models.CharField(max_length=30,null=True,blank=True)
    # 抓包字段添加
    catch_url=models.CharField(max_length=30,null=True,blank=True,default='')
    mock_response_body=models.TextField(null=True,blank=True,default='')
    response_headers = models.CharField(max_length=500, null=True, blank=True, default='{}')
    model=models.CharField(max_length=30,null=True,blank=True,default='Release') # Interceptor Release
    state_code=models.IntegerField(default=200)
    mock_response_body_lj = models.TextField(null=True, blank=True, default='')  # 拦截模式的写死的返回值
    mock_time=models.FloatField(default=0) # 整个请求周期时间控制

    def __str__(self):
        return self.name