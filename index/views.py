from .forms import RegForm
from .send_email import *
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
STARTED = False


def index(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            data = form.data
            course_name = {
                'phy9': 'Физика 9',
                'phy11': 'Физика 11',
                'math1011': 'Математика 10-11'
            }
            send_email(data['name'], data['email'], data['phone'], course_name[data['programs']], STARTED)
            apply = Apply(name=data['name'], email=data['email'], phone=data['phone'], program=data['programs'])
            apply.save()
            form = RegForm()
    else:
        form = RegForm()
    return render(request, 'html/index.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lk')
        else:
            messages.success(request, "Неправильный логин или пароль, попробуйте снова")
            return redirect('login')
    else:
        return render(request, 'html/login.html', {})


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


def page_not_found_view(request, exception):
    return render(request, 'html/404.html', status=404)


class SitemapXmlView(TemplateView):
    template_name = 'sitemap.xml'
    content_type = 'text/plain'
