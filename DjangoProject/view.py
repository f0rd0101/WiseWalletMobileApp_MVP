from django.shortcuts import render

def main_view(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def market_page(request):
    return render(request, 'market.html')
def settings_page(request):
    return render(request, 'settings.html')

def main_vip_view(request):
    return render(request,'index_vip.html')

def market_page_vip(request):
    return render(request, 'market_vip.html')
def settings_vip_view(request):
    return render(request,'settings_vip.html')