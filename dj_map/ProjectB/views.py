from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
import requests
from .forms import MakeProductForm



def show_products(request):
    response = requests.get('http://127.0.0.1:8000/api/products/')
    products = response.json()
    print(products)

    return render(request, "products.html", {'products': products})
    pass


class MakeProduct(View):
    def get(self, request):
        
        form = MakeProductForm()
        return render(request, 'make-product.html', {'form': form})

    def post(self, request):
        form = MakeProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            photo = form.cleaned_data['photo']

            response = requests.post('http://127.0.0.1:8000/api/products/')
            send_products = response.json(name, description, category, price, photo)
            print(send_products)
        return render(request, 'make-product.html', {'form': form})





