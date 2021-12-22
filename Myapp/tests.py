from django.test import TestCase

# Create your tests here.
# l=['1','2','3']
# l[:]=l[1:]+l[:-1]
#
# print(l)
"""
列表转换为str，用split
str转换为列表，用join
强制转换不建议
"""
# def func(a,b=1,*anything):
#     print(a)
#     print(b)
#     print("args:",anything)
#
# def funca(**kwargs):
#     print("kwargs:",kwargs)
#
# def funcb(*args,**anything):
#     print("args=",args)
#     print("anything=",anything)
#
# if __name__ == "__main__":
#    func(0,1,'无敌哥流批',[22,33],44)
#    print("---我是分割线---")
#    funca(a=1,b=2,c=3)
#    print("---我是分割线---")
#    funcb([0,1,"t"],1,None,a=1,b=2,c=3)

# old={'a':{'b':{'c':1,'m':2}}}
# x='a.b.c="abc"'
# key=x.split('=')[0].rsplit()
# key1=''.join(key)
# print(key1)
# # value=x.split('=')[1].lstrip()
# # print(value)
# for i in key1.split('.'):
#     print(i)

new={"a":{"b":{"c":21,"m":2}}}
y= 'a.b.c = 123'
"""
期望：
old['a']['b']['c']=value
"""
key=y.split('=')[0].rstrip() #rstrip() 函数作用：去除右边空格
value=eval(y.split('=')[1].lstrip())#eval() 函数作用：能把字符串转化成python的各种数据类型

tmp_cmd=''
for i in key.split('.'):
    try:
        int(i)
        tmp_cmd+="[%s]"%i
    except:
        tmp_cmd+="[%s]"%repr(i) #repr() 函数作用：去除右边空格

end_cmd='new'+tmp_cmd+"=value"
print(end_cmd)
exec(end_cmd) #exec() 函数作用：执行python环境命令
print(new)


# 切片法  包左不包右
# 字符串不能修改，字符串转列表可以直接转，转化后就可切片
# 修改字符串实现方法二：  拼接法 利用左必右开
# 字符串replace后，原始的不会变；replace后新增一个字符串会是目标值