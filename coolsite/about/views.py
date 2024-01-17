from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def index(request):
    return HttpResponse("Страница приложения about")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render(request, 'about/header.html')
def about(request):
    return render(request, 'about/footer.html')
def about(request):
    return render(request, 'about/base.html')