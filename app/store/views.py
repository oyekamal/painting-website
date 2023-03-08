from django.shortcuts import get_object_or_404, redirect, render

from django.db.models import Q


# Create your views here.


def home(request):
    return render(request, "store/home.html")


def about(request):
    return render(request, "store/about.html")
