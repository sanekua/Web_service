from django.shortcuts import render
import time
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

