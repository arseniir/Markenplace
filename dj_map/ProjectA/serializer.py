from rest_framework import serializers
from .models import MakeProductModel, CommentFeedbackModel






class MakeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeProductModel
        fields = '__all__'


 


class CommentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFeedbackModel
        fields = '__all__'
