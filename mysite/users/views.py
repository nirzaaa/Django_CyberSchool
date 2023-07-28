from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ResumeUpdateForm, PresentUpdateForm
from .models import Resume

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)    

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def resume(request):

    if request.method == 'POST':
        r_form = ResumeUpdateForm(request.POST, request.FILES, instance=request.user.resume)

        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'Your resume has been updated!')

            my_pickle()
            return redirect('profile')
        
    else:
        r_form = ResumeUpdateForm(instance=request.user.resume)

    context = {
        'r_form': r_form
    }

    return render(request, 'users/resume.html', context)

def my_pickle():
    import glob
    import os
    import pickle

    list_of_files = glob.glob('./media/resume_files/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    with open(latest_file, 'rb') as f:
        output = pickle.load(f) # deserialize using load()
        # print(output) # print student names

@login_required
def present(request):

    if request.method == 'POST':
        r_form = PresentUpdateForm(request.POST, request.FILES, instance=request.user.present)

        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'Your present has been updated!')

            secure = request.POST.get("secure")

            data_list = my_present(secure)

            if not isinstance(data_list, list):
                return render(request, 'users/present.html', {'error': True, data_list: None})

            else:
                context = {
                    'data_list': data_list,
                    'r_form': r_form
                }


                return render(request, 'users/present.html', context)
        
    else:
        r_form = PresentUpdateForm(instance=request.user.present)

    context = {
        'r_form': r_form
    }

    return render(request, 'users/present.html', context)

def my_present(secure):
    

    from django.http import HttpResponse

    import glob
    import os
    import json

    list_of_files = glob.glob('./media/present_files/*')
    latest_file = max(list_of_files, key=os.path.getctime)

    try:
        if secure:
            import defusedxml.ElementTree as ET
        else:
            import xml.etree.ElementTree as ET

        with open(latest_file, 'r') as f:
            document = ET.parse(f)

        root = document.getroot()
        
        data_list = list()

        for x in root:
            data_list.append((x.tag, x.text))
        
    except Exception as x:
        data_list = x


    return data_list
