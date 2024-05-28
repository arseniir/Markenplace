from django.urls import path
from ProjectA.views import MakeProductAPIView, UpdateProductView, CommentFeedbackView, UpdateCommentFeedbackView



urlpatterns = [
    # make product
    path('api/products/', MakeProductAPIView.as_view(), name='product-detail'),
    path('api/products/<int:pk>/', UpdateProductView.as_view(), name='action-on-page'),
    
    # add comment
    path('api/comment/', CommentFeedbackView.as_view(), name='add-comment'),
    path('api/comment/<int:pk>/', UpdateCommentFeedbackView.as_view(), name='add-comment_id')




]