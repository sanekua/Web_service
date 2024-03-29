"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path, include
from users import views as users_views
from web import views as web_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('register/', users_views.register, name='register'),
    #path('upload/', users_views.profile, name='upload'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #
    path('h', users_views.Home.as_view(), name='home1'),
    path('upload/', users_views.upload, name='upload'),
    path('books/', users_views.book_list, name='book_list'),
    path('upload_book/', users_views.upload_book, name='upload_book'),
    path('books/<int:pk>/', users_views.delete_book, name='delete_book'),

    path('class/books/', users_views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', users_views.UploadBookView.as_view(), name='class_upload_book'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)