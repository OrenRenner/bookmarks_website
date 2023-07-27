from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm, UserRegistrationForm


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


def register(requset):
    if requset.method == "POST":
        user_form = UserRegistrationForm(requset.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базе данных
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль
            new_user.set_password(user_form.cleaned_data["password"])
            # Сохраняем пользователя в базе данных
            new_user.save()
            return render(requset, "account/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(requset, "account/register.html", {"user_form": user_form})