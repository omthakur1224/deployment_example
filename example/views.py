from django.shortcuts import render

# Create your views here.
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Welcome</h1>
            <h2>The current time is { now }.</h2>
        </body>
    </html>
    '''
    return HttpResponse(html)
