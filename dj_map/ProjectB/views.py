from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
import requests
from .forms import MakeProductForm, UpdateDeleteProductForm, DeleteProductForm, CommentFeedbackForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



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




    
@method_decorator(csrf_exempt, name='dispatch') 
class UpdateDeleteProduct(View):
    def get(self, request, product_id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{product_id}/')
        if response.status_code == 200:
            product = response.json()
            form = UpdateDeleteProductForm(initial=product)  
            return render(request, 'changes.html', {'form': form, 'product_id': product_id})
        else:
            return HttpResponseNotFound()

    def post(self, request, product_id):
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
                return render(request, 'changes.html', {'product_id': product_id})  
            else:
                error_message = "Error: " + response.text  
                # print(response.text)
                return render(request, 'changes.html', {'form': form, 'error_message': error_message, 'product_id': product_id})
        
        return render(request, 'changes.html', {'form': form, 'product_id': product_id})




    
class DeleteProductView(View):
    def get(self, request, id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{id}/')
        if response.status_code == 200:
            product = response.json()
            form_delete = DeleteProductForm(initial=product)  
            return render(request, 'delete-product.html', {'form_delete': form_delete, 'id': id})
        else:
            return HttpResponseNotFound()
        
    def post(self, request, id):
        form_delete = UpdateDeleteProductForm(request.POST)
        if form_delete.is_valid():
            point = form_delete.cleaned_data['point']
            if point == 'delete':
                response = requests.delete(f'http://127.0.0.1:8000/api/products/{id}/')
                if response.status_code == 204: 
                    delete_product = response.json()
                    return redirect('/update-product/')  # Перенаправлення після успішного видалення
                else:
                    error_message = "Error: " + response.text  
                    print(response.text)
                    return render(request, 'delete-product.html', {'form_delete': form_delete, 'error_message': error_message, 'id': id})
        # Повернення форми у випадку невдачі або якщо точка видалення не вибрана
        return render(request, 'delete-product.html', {'form_delete': form_delete, 'id': id})
    

# -------------------------------------------------------------------------------
class CreateComment(View):
    def get(self, request, id):
        form = CommentFeedbackForm()
        return render(request, 'comment.html', {'form': form, 'id': id})

    def post(self, request, id):
        form = CommentFeedbackForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')  
            feedback = form.cleaned_data.get('feedback')
            
            data = {
                'comment': comment,
                'feedback': feedback,
            }

            response = requests.post(f'http://127.0.0.1:8000/api/comment/{id}/', data=data)

            if response.status_code == 201: 
                send_products = response.json()
                print(send_products)
                return render(request, 'comment.html')  
            else:
                error_message = "Error."
                return render(request, 'comment.html', {'form': form, 'error_message': error_message, 'id': id})
        
        return render(request, 'comment.html', {'form': form, 'id': id})


def all_comments(request):
    response = requests.get('http://127.0.0.1:8000/api/comment/')
    purchases = response.json()
    print(purchases)
    return render(request, "comment.html", {'purchases': purchases,})
    pass
