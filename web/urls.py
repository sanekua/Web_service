from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-about')
]