from django.shortcuts import render

def main_view(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def market_page(request):
    return render(request, 'market.html')
def settings_page(request):
    return render(request, 'settings.html')