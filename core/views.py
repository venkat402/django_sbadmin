from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.forms import AuthenticationForm

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            # message = render_to_string('account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def error_404_view(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


@login_required
def index(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'index.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


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


def account_activation_sent(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'utilities-other.html', data)


def activate(request, uidb64, token):
    # try:
    #     # uid = force_text(urlsafe_base64_decode(uidb64))
    #     uid = urlsafe_base64_encode(force_bytes(uidb64)).decode(),
    #     user = User.objects.get(pk=uid)
    # except (TypeError, ValueError, OverflowError, User.DoesNotExist):
    #     user = None

    message = render_to_string('account_activation_email.html', {
        # 'user': user,
        # 'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(uidb64)).decode(),
        'token': token,
    })
    # if user is not None and account_activation_token.check_token(user, token):
    #     user.is_active = True
    #     user.profile.email_confirmed = True
    #     user.save()
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     return render(request, 'account_activation_invalid.html')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "mails/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="forgot-password.html",
                  context={"password_reset_form": password_reset_form})
