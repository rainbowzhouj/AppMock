from django.test import TestCase

# Create your tests here.
l=['1','2','3']
l[:]=l[1:]+l[:-1]

print(l)
"""
列表转换为str，用split
str转换为列表，用join
强制转换不建议
"""