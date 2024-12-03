from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(reqest):
    return render(reqest, "index.html")


def about(reqest):
    return render(reqest, "about.html")

def services(reqest):
    return render(reqest, "services.html")

def blog(reqest):
    return render(reqest, "blog.html")

def contact(reqest):
    return render(reqest, "contact.html")

def mannual(reqest):
    return render(reqest, "mannual.html")
