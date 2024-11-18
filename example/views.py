from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
# views.py
from django.http import JsonResponse




def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


def modify_hello(request):
    if request.method == "GET":
        input_text = request.GET.get("text", "Hello")
        return JsonResponse({"message": f"{input_text} Vercel"})
