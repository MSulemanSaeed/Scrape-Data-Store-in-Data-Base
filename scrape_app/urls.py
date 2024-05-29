
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('scrape_books', views.scrape_books),
]
