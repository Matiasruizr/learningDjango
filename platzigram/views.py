""" Platzigram Views"""
from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y -%H:%M hrs ')
    return HttpResponse('hello world, the current server time is  {now}'.format(now = str(now)))

def sorted_integers(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    data = {
        'status' : 'ok',
        'numbers': numbers,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse( json.dumps(data, indent= 4), content_type='application/json')

def say_hi(request, name, age):
    if age < 18:            
        autorizado = False
    else:
        autorizado = True

    data = {
        'status' : 'ok',
        'nombre' : name,
        'edad' : age,
        'autorizado': autorizado
    } 
    return HttpResponse(json.dumps(data, indent= 4), content_type = 'application/json')
