from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



# def home(request):
#     return render(request,'web/home.html')
#
# def about(request):
#     return render(request, 'web/about.html')



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)


def about(request):
    return render(request, 'web/about.html', {'title': 'About'})



def upload(request):
    return render(request, 'web/upload.html', {'title': 'Upload'})


