from django.http import HttpResponse
from django.http import JsonResponse
import pdb 
#utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M HRS')
    return HttpResponse(f'Oh hi,Hello World time is {now}')

def hi(request):
    numbers = (request.GET['numbers'])
    print(f'numbers one line {numbers}')
    order = sorted(numbers.split(','))
    print(order)    
    response = JsonResponse(order, safe=False)
    return response

def say_hi(request, name, age):
    """return a greeting """
    if age < 12:
        message = "Sorry " + name + ", you are not allowed here"
    else:
        message = "Hello, " + name + " welcome to Platzigram"
    return HttpResponse(message)

    