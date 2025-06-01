
from django.contrib import admin
from django.urls import path
from DjangoProject.view import main_view
from DjangoProject.view import login_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view, name='home'),
    path('login/',login_page, name='login'),

]
