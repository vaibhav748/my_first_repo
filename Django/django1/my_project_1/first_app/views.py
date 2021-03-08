from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1>This is the Home Page.</h1> <a href='contact/'>Contact</a> | <a href='about/'>About</a>")
    my_dict = {'name': "John"}
    return render(request, 'first_app/index.html', context=my_dict)


def contact(request):
    return HttpResponse(
        "<h1>This is the Contact Page.</h1> <a href='/customer'>Home</a> | <a href='/customer/about'>About</a>")


def about(request):
    return HttpResponse(
        "<h1>This is the About Page</h1> <a href='/customer/contact/'>Contact</a> | <a href='/customer'>Home</a>")
