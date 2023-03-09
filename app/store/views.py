from django.shortcuts import get_object_or_404, redirect, render

from django.db.models import Q


# Create your views here.


def home(request):
    return render(request, "store/home.html")


def about(request):
    return render(request, "store/about.html")


def products(request):
    return render(request, "store/products.html")


def blog(request):
    return render(request, "store/blog.html")

def blog_details(request):
    return render(request, "store/blog-details.html")

def contact(request):
    return render(request, "store/contact.html")