
from django.contrib import admin
from django.urls import path
from DjangoProject.view import main_view;
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view, name='home'),
]
