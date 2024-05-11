from django.urls import path
from ProjectB.views import show_products, MakeProduct



urlpatterns = [
    # make product
    path('', show_products, name='products'),
    path('make_products/', MakeProduct.as_view(), name='make_products')

]