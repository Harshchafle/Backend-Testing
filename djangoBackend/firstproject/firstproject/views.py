from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About Page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Contact Page")
    return render(request, 'contact.html')

def services(request):
    #return HttpResponse("Services Page")
    return render(request, 'services.html')

def portfolio(request):
    #return HttpResponse("Portfolio Page")
    return render(request, 'portfolio.html')

def blog(request):
    #return HttpResponse("Blog Page")
    return render(request, 'blog.html')

def faq(request):
    #return HttpResponse("FAQ Page") 
    return render(request, 'faq.html')