from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm, FilesUpdateForm#,FilesUpdateForm1
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

import time

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        t_form = FilesUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid and t_form.is_valid:
            u_form.save()
            p_form.save()
            t_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        t_form = FilesUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        't_form': t_form,

    }
    return render(request, 'users/profile.html', context)


#
# @login_required
# def prof(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         # p_form = ProfileUpdateForm(request.POST,
#         #                            request.FILES,
#         #                            instance=request.user.profile)
#         t_form = FilesUpdateForm1(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and t_form.is_valid:
#             u_form.save()
#             #p_form.save()
#             t_form.save()
#             messages.success(request, f'Your file has been updated!')
#             return redirect('upload')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         #p_form = ProfileUpdateForm(instance=request.user.profile)
#         t_form = FilesUpdateForm1(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         't_form': t_form,
#
#     }
#     return render(request, 'users/prof.html', context)
