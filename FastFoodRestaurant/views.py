from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def book_view(request):
    return render(request,'book.html')

def menu_view(request):
    return render(request,'menu.html')

# Create your views here.
