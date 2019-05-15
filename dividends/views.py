from django.shortcuts import render

def index(request):
    return render(request, 'dividends/dividends.html')

def dividend(request):
    return render(request, 'dividends/dividends.html')

def search(request):
    return render(request, 'dividends/search.html')
