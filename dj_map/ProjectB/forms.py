from django import forms
from ProjectA.models import MakeProductModel, CommentFeedbackModel

class MakeProductForm(forms.ModelForm):
    class Meta:
        model = MakeProductModel
        fields = ['name', 'description', 'category', 'price', 'photo']

class CommentFeedbackForm(forms.Form):
    class Meta:
        model = CommentFeedbackModel
        fields = ['comment', 'feedback']