from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import userForm, profilForm


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = userForm(request.POST, request.FILES)
        profile_form = profilForm(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)

            profil = profile_form.save(commit=False)
            profil.user = user

            user.save()
            profil.save()

            return redirect("/")
    else:
        form = userForm()
    proForm = profilForm()

    return render(request, "accounts/register.html", {"form": form, "proForm": proForm})


@login_required
def profil(request):
    return render(request, "accounts/profil.html")
