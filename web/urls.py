from . import views
from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='web-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-form'),
    path('about/', views.about, name='web-about'),
]