from __future__ import absolute_import, unicode_literals
from dcs.celeryconf import app
import time

from django.core.mail import EmailMessage

@app.task(bind=True, ignore_result=False, max_retries=3)
def demo_task1(self):
    result = {
        'val1': 1,
        'val2': 2,
        'val3': 3,
    }
    print("hellp")
    from_email = 'testmyserverwebsite@gmail.com'
    to_list = ['robomex2020@gmail.com',]
    sendemail = EmailMessage("Message received!!!", "Hello test", str(from_email), to_list)
    sendemail.send()
    return result

