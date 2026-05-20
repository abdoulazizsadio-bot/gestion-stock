from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
def articles(request):
    return render(request, 'articles.html')

def templates_base(request):
    return render(request, 'Templates_base.html')