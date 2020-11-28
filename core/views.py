from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


def index(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'index.html', data)


def test(request):
    return HttpResponse("Hello, world. You're at the Home page of Django sample project error 404.")


def error_404(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


def blank(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'blank.html', data)


def buttons(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'buttons.html', data)


def cards(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'cards.html', data)


def charts(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'charts.html', data)


def forgot_password(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'forgot-password.html', data)


def login(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'login.html', data)


def register(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'register.html', data)


def tables(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'tables.html', data)


def u_animation(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'utilities-animation.html', data)


def u_border(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'utilities-border.html', data)


def u_color(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'utilities-color.html', data)


def u_other(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'utilities-other.html', data)
