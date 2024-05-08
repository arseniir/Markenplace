from django.contrib import admin
from .models import MakeProductModel, CommentFeedbackModel

class MakeProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'photo')
admin.site.register(MakeProductModel, MakeProductAdmin)


class CommentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('comment', 'feedback')
admin.site.register(CommentFeedbackModel, CommentFeedbackAdmin)