from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


User = get_user_model()


def home_page(request):
    context = {
        'title': "Hello, World!",
        'content': "Welcome to our homepage"
    }
    if request.user.is_authenticated():
        context['premium_content'] = "YAAAAAAAAAAAY"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': "About Page",
        'content': "People > Technology"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    form_class = ContactForm(request.POST or None)
    context = {
        'title': "Contact Us!",
        'content': "We'll be happy to talk to you",
        'form': form_class
    }
    if form_class.is_valid():
        print(form_class.cleaned_data)
    # if request.method == 'POST':
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form_class = LoginForm(request.POST or None)
    context = {
        "form": form_class
    }
    print("User logged {}".format(
        "in" if request.user.is_authenticated() else "off")
    )
    if form_class.is_valid():
        print(form_class.cleaned_data)
        username = form_class.cleaned_data.get("username")
        password = form_class.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # context['form'] = LoginForm()
            redirect("/")
        else:
            print("Error Logging in")
    return render(request, "auth/login.html", context)


def register_page(request):
    form_class = RegisterForm(request.POST or None)
    context = {
        'form': form_class
    }
    if form_class.is_valid():
        username = form_class.cleaned_data.get("username")
        email = form_class.cleaned_data.get("email")
        password = form_class.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
