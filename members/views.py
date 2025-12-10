from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    print(request.path,'^_^',flush=True)
    return render(request, "index.html")


def greet(request):
    print(request.path,'!!',flush=True)
    return HttpResponse("Hi ~ Greeting from Django.")