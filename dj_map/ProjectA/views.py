from django.shortcuts import render
from rest_framework import generics
from .models import MakeProductModel
from .serializer import MakeProductSerializer


class MakeProductAPIView(generics.ListCreateAPIView):
    queryset = MakeProductModel.objects.all()
    serializer_class = MakeProductSerializer


def show(request):
    products = MakeProductModel.objects.all()
    return render(request, 'purchase.html', {'products': products})