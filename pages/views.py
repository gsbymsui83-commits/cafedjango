from django.shortcuts import render

def intro_page(request):
    return render(request, 'pages/intro_page.html')

def location_page(request):
    return render(request, 'pages/location_page.html')