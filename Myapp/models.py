from django.db import models

# Create your models here.
class DB_project(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    creator=models.CharField(max_length=30,null=True,blank=True)
    run_counts=models.IntegerField(default=0)
    mocks_counts=models.IntegerField(default=0)
    state=models.BooleanField(default= False) #服务状态
    def __str__(self):
        return '项目名字是'+self.name

class DB_mock(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    state=models.BooleanField(default=False)
    project_id=models.CharField(max_length=30,null=True,blank=True)
    # 抓包字段添加
    catch_url=models.CharField(max_length=30,null=True,blank=True,default='')
    mock_response_body=models.TextField(null=True,blank=True,default='')
    def __str__(self):
        return self.name