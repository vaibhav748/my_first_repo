from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunction1(request):
    return HttpResponse("This is the firstpage of app2.")

def myfunction2(request):
    return HttpResponse("This is the secondpage of app2.")