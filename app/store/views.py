from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    return render(request, "store/home.html")


def about(request):
    return render(request, "store/about.html")


def products(request):
    painting_list = Painting.objects.all().order_by("created_at")
    page = request.GET.get('page', 1)
    paginator = Paginator(painting_list, per_page=1)
    try:
        paintings = paginator.page(page)
    except PageNotAnInteger:
        paintings = paginator.page(1)
    except EmptyPage:
        paintings = paginator.page(paginator.num_pages)
    context = {"paintings": paintings}
    print(paintings.has_other_pages )
    return render(request, "store/products.html",context)

class PaintingDetailView(DetailView):
    model = Painting
    template_name = 'store/painting_detail.html'

def blog(request):
    return render(request, "store/blog.html")

def blog_details(request):
    return render(request, "store/blog-details.html")

def contact(request):
    return render(request, "store/contact.html")