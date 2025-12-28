from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm


# =========================
# REGISTER
# =========================
def register_view(request):
    form = RegisterForm(request.POST or None)

    # Ajout des classes Bootstrap
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        messages.success(request, "Compte créé avec succès 🎉")
        login(request, user)
        return redirect('dashboard')

    return render(request, 'accounts/register.html', {'form': form})


# =========================
# LOGIN
# =========================
def login_view(request):
    form = AuthenticationForm(data=request.POST or None)

    # Ajout des classes Bootstrap
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    if form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Connexion réussie 👋")
        return redirect('dashboard')

    if request.method == "POST":
        messages.error(request, "Nom d’utilisateur ou mot de passe incorrect")

    return render(request, 'accounts/login.html', {'form': form})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté")
    return redirect('login')


# =========================
# DASHBOARD
# =========================
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
