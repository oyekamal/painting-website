from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("products", views.products, name="products"),
    path("blog", views.blog, name="blog"),
    path("blog-details", views.blog_details, name="blog_details"),
]

