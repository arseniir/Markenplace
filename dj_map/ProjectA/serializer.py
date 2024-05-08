from rest_framework import serializers
from .models import MakeProductModel


# class MakeProductMa:
#     def __init__(self, name, description, category, price, photo):
#         self.name = name
#         self.description = description
#         self.category = category
#         self.price = price
#         self.photo = photo



class MakeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeProductModel
        fields = '__all__'


    def create(self, validated_data):
        return MakeProductModel.objects.create(**validated_data)
