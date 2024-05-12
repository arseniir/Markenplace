from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
import requests
from .forms import MakeProductForm, UpdateDeleteProductForm





def show_products(request):
    response = requests.get('http://127.0.0.1:8000/api/products/')
    products = response.json()
    # print(products)

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

            data = {
                'name': name,
                'description': description,
                'category': category,
                'price': price,
            }
            files = {'photo': request.FILES['photo']} if 'photo' in request.FILES else None

            response = requests.post('http://127.0.0.1:8000/api/products/', data=data, files=files)


            error_message = None  

            if response.status_code == 201: 
                send_products = response.json()
                print(send_products)
                return render(request, 'make-product.html')  
            else:
                error_message = "Error."
                return render(request, 'make-product.html', {'form': form, 'error_message': error_message})
                pass
        
        return render(request, 'make-product.html', {'form': form})
    




def all_products(request):
    response = requests.get('http://127.0.0.1:8000/api/products/')
    purchases = response.json()
    print(purchases)
    return render(request, "update-product.html", {'purchases': purchases})
    pass




    

class UpdateDeleteProduct(View):
    def get(self, request, product_id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{product_id}/')
        if response.status_code == 200:
            product = response.json()
            form = UpdateDeleteProductForm()  
            return render(request, 'changes.html', {'form': form})
        else:
            return HttpResponseNotFound()

    def put(self, request, product_id):
        form = UpdateDeleteProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            photo = form.cleaned_data['photo']

            data = {
                'name': name,
                'description': description,
                'category': category,
                'price': price,
            }
            files = {'photo': request.FILES['photo']} if 'photo' in request.FILES else None

            response = requests.put(f'http://127.0.0.1:8000/api/products/{product_id}/', data=data, files=files)

            error_message = None  

            if response.status_code == 200: 
                send_products = response.json()
                print(send_products)
                return render(request, 'changes.html')  
            else:
                error_message = "Error: " + response.text  
                print(response.text)
                return render(request, 'changes.html', {'form': form, 'error_message': error_message})
        
        return render(request, 'changes.html', {'form': form})






   










