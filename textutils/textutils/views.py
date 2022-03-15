# I have created this file - Manisha
from django.http import HttpResponse
from django.shortcuts import render


# views here
def index(request):
    return render(request, 'index.html')


def removepunc(request):
    # GET THE TEXT FROM GET REQUEST PARAMS
    reqText = request.GET.get('text', 'default')
    print(reqText)
    return HttpResponse("removepunc")


def capitalizefirst(request):
    return HttpResponse("capitalizefirst")


def newlineremove(request):
    return HttpResponse('newlineremove')


def spaceremove(request):
    return HttpResponse('spaceremove')


def charactercounte(request):
    return HttpResponse('charactercounte')


def titlecase(request):
    return HttpResponse('titlecase')
