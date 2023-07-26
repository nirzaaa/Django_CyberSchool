from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreateNewPost, Calculation
from django.http import HttpResponse, HttpResponseRedirect
import os
import re
from .forms import Ssti

# Create your views here.

def home(response):
    context = {
        'vulns': ["IDOR", "SQLI", "RCE"]
    }

    return render(response, "main/home.html", context)

def about(response):

    return render(response, "main/about.html")

# @login_required
def idor(response):

    return render(response, "main/idor.html")

def xss(response):
    context = {
        'posts': Post.objects.all()
    }
    return render(response, "main/xss.html", context)

def sqli(response):

    return render(response, "main/sqli.html")

def rce(response):

    context = {
        'posts': Post.objects.all()
    }

    return render(response, "main/rce.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'main/idor.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

# ==== The vulnerable class ==== #

# class PostDetailView(DetailView):
#     model = Post

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
# ============================== #

# ==== The patch ==== #

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# ===================== #

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def calculation(response):
    if response.method == "POST":
        form = Calculation(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = form.cleaned_data["text"]
        
        # ==== The vulnetable code ==== #
        print(t)
        result = eval(t)
        return render(response, "main/show.html", {"t":t, "result":result, "hacker":False})

        # ============================= #

        # ==== The patch ==== #

        x = re.match("[a-zA-Z]", t)
        if x:
            hacker = True
            return render(response, "main/show.html", {"hacker":hacker})
        else:
            hacker = False
            result = eval(t)
            return render(response, "main/show.html", {"t":t, "result":result, "hacker":hacker})

        # =================== #

    else:
        form = Calculation()
    return render(response, "main/calculation.html", {"form":form})



def show(response):

    return render(response, "main/show.html")

def ssti(request):

    from jinja2 import Template

    cmd = request.GET.get("cmd")
    
    template = Template(f'Hello {cmd}!')

    if cmd:
        print(template.render())
        return HttpResponse("Thank you for the input")
    else:
        return HttpResponse("No input provided - enter ?cmd=")

    # ====== patch 1 ====== # 

    # cmd = request.GET.get("cmd")

    # if cmd:
    #     return render(request, 'main/ssti_vul.html', {'cmd':cmd})
    # else:
    #     return HttpResponse("No input provided")


    # ====== patch 2 ====== #

    # s_form = Ssti()

    # context = {
    #     's_form': s_form,
    # }

    # return render(request, 'main/ssti.html', context)

def login_cookie(request):
    # request.session['visit'] = 0
    if request.method == "GET":
        # getting cookies
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'main/home_cookie.html', context)
        else:
            return render(request, 'main/login_cookie.html')

    if request.method == "POST":
        username=request.POST.get('username')
        context = {
                'username':username,
                'login_status':'TRUE',
            }
        response = render(request, 'main/home_cookie.html', context)

        # setting cookies
        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response

def home_cookie(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'main/home_cookie.html', context)
    else:
        return render(request, 'main/home_cookie.html')


def logout_cookie(request):
    response = HttpResponseRedirect(reverse('login'))

    # deleting cookies
    response.delete_cookie('username')
    response.delete_cookie('logged_in')

    return response

def count_visit(request):
    visit = request.session.get('visit',0) + 1
    request.session['visit'] = visit
    return HttpResponse(f"Visit count:{request.session['visit']}")

def lfi(request):

    cmd = request.GET.get("cmd")
    

    if cmd:
        return render(request, 'main/lfi.html', context={"cmd":cmd})
    else:
        return HttpResponse("No input provided - enter ?cmd=")

