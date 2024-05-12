from django.urls import path
from ProjectB.views import show_products, MakeProduct, all_products, UpdateDeleteProduct
# from . import views


urlpatterns = [
    # make product
    path('', show_products, name='products'),
    path('make_products/', MakeProduct.as_view(), name='make_products'),

    path('update_products/<int:product_id>/', UpdateDeleteProduct.as_view(), name='update_product_id'),
    path('update_products/', all_products ,name='update_products' ),
]
