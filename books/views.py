from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Ad
from django.http import HttpResponse

# Create your views here.


def home(request):
    products1 = [
        {"name": "Abhishek Varde", "des": "My age is abhishek my age is 21", "price": 1000},
        {"name": "Purva Nalat", "des": "I am his girlfriend and i'm here to help him in project.", "price": "fuck off"},
        {"name": "Abhishek Varde", "des": "My age is abhishek my age is 21", "price": 1000},
        {"name": "Purva Nalat", "des": "I am his girlfriend and i'm here to help him in project.", "price": "fuck off"},
        {"name": "Abhishek Varde", "des": "My age is abhishek my age is 21", "price": 1000},
        {"name": "Purva Nalat", "des": "I am his girlfriend and i'm here to help him in project.", "price": "fuck off"},
        {"name": "Abhishek Varde", "des": "My age is abhishek my age is 21", "price": 1000},
        {"name": "Purva Nalat", "des": "I am his girlfriend and i'm here to help him in project.", "price": "fuck off"},
        {"name": "Abhishek Varde", "des": "My age is abhishek my age is 21", "price": 1000},
    ]

    products = Ad.objects.all()

    paginator = Paginator(products, 15)  # Show 15 contacts per page

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, "books/index.html", {'products': products})


def product_page(request):
    id = request.GET.get('id')
    product_details = Ad.objects.get(id=id)
    return render(request, "books/product_page.html", {"product_details": product_details})
