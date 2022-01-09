#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import threading
import time
import django
import os, sys
sys.path.append('/Users/zhoujing/PycharmProjects/AppMock')
os.environ.setdefault("DJANGO_SETTINGS_MODULE","AppMock.settings")
django.setup()
from Myapp.models import *

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppMock.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def monitor_thread():
    '巡逻官线程'
    while True:
        time.sleep(1800)
        projects=DB_project.objects.all()
        for p in projects:
            if p.catch==True:
                cha=int(time.time())-int(p.catch_time)
                if cha>10:
                    print("发现一个没关的项目",p.name)
                    p.catch=False
                    p.save()




if __name__ == '__main__':
    t = threading.Thread(target=monitor_thread)
    t.setDaemon(True)
    t.start()
    main()
