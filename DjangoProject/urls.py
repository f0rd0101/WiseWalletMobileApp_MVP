
from django.contrib import admin
from django.urls import path
from DjangoProject.view import main_view
from DjangoProject.view import login_page
from DjangoProject.view import  market_page
from DjangoProject.view import settings_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view, name='home'),
    path('login/',login_page, name='login'),
    path('market/',market_page, name='market'),
    path('settings/',settings_page, name='settings'),
]
