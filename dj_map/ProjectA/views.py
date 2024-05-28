from rest_framework import generics
from .models import MakeProductModel, CommentFeedbackModel
from .serializer import MakeProductSerializer, CommentFeedbackSerializer


# make product
class MakeProductAPIView(generics.ListCreateAPIView):
    queryset = MakeProductModel.objects.all()
    serializer_class = MakeProductSerializer


class UpdateProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MakeProductModel.objects.all()
    serializer_class = MakeProductSerializer



# add comment
class CommentFeedbackView(generics.ListCreateAPIView):
    queryset = CommentFeedbackModel.objects.all()
    serializer_class = CommentFeedbackSerializer


class UpdateCommentFeedbackView(generics.CreateAPIView):
    queryset = CommentFeedbackModel.objects.all()
    serializer_class = CommentFeedbackSerializer







    









# class MakeProductAPIView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_detail.html'

#     def get(self, request, pk):
#         product = get_object_or_404(MakeProductModel, pk=pk)
#         serializer = MakeProductSerializer(product)
#         return Response({'serializer': serializer, 'profile': product})

#     def post(self, request, pk):
#         product = get_object_or_404(MakeProductModel, pk=pk)
#         serializer = MakeProductSerializer(product, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'product': product})
#         serializer.save()
#         return redirect('add-product')
