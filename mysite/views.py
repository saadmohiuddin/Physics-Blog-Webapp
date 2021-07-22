from django.http import HttpResponse
from datetime import datetime



def hello(request):
    return HttpResponse("Hello World")

def currentTime(request):
    now=datetime.now()
    html="<html><body>The current time is %s</body></html>" %now

    return HttpResponse(html)

def hours_ahead(request,offset):
    now=datetime.now()
    time = now + timedelta(hours=offset)
    html="<html><body>The time after hours is %s</body></html>"%time
    return HttpResponse(html)
