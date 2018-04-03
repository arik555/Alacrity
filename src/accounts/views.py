from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MyLoginForm, MyRegisterForm
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse("Please logout first n then login.")
    title = "Login"
    form = MyLoginForm()

    if request.method == 'POST':
        form = MyLoginForm(request.POST)

        if form.is_valid():
            uname = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            user = authenticate(username=uname, password=pswd)
            login(request, user)
            # redirect to some page
            return redirect("/")

    my_dict = {"form": form, 'title': title}
    return render(request, 'myform.html', context=my_dict)


def register_user(request):
    if not request.user.is_superuser:
        return HttpResponse('Page not found.')
    title = "Register"
    form = MyRegisterForm()

    if request.method == "POST":
        form = MyRegisterForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            pswd = form.cleaned_data['password']
            instance.set_password(pswd)
            instance.save()
            user = authenticate(username=instance.username, password=pswd)
            login(request, user)
            # redirect to some page
            return redirect("/")

    my_dict = {'form': form, 'title': title}
    return render(request, "myform.html", context=my_dict)


def logout_user(request):
    logout(request)
    return redirect("/")
