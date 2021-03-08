from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunction(request):
    return HttpResponse("Hello World.")

def about(request):
    return HttpResponse("This is my first project.")

def myfirstpage(request):
    return render(request, "index.html")

def mysecondpage(request):
    return render(request, "second.html")

def mythirdpage(request):
    var = "this is django"
    greeting = "Good Morning"
    my_fruits = ['a', 'b', 'c']
    my_dict = {
        "var": var,
        "greeting": greeting,
        "fruits": my_fruits
    }
    return render(request, "third.html", context = my_dict)