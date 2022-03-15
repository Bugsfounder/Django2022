# I have created this file - Manisha
from django.http import  HttpResponse

# views here
def index(request):
    return  HttpResponse('<h1>Hello Manisha</h1>')

def about(request):
    return HttpResponse("<h1>Hello About Page Created By Manisha</h1>")
