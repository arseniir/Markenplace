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


class UpdateCommentFeedbackView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentFeedbackModel.objects.all()
    serializer_class = CommentFeedbackSerializer




# class MakeProductAPIView(View):
#     def get(self, request):
#         makeproduct = MakeProductForm()
#         return render(request, 'add_product.html', {'makeproduct': makeproduct})
    
#     def post(self, request):
#         makeproduct = MakeProductForm(request.POST)
#         if makeproduct.is_valid():
#             name = makeproduct.cleaned_data['name']
#             description = makeproduct.cleaned_data['description']
#             category = makeproduct.cleaned_data['category']
#             price = makeproduct.cleaned_data['price']
#             photo = makeproduct.cleaned_data['photo']

#             fi = MakeProductModel.objects.create(name=name, description=description, category=category, price=price, photo=photo)
#             fi.save()
#         return render(request, 'add_product.html', {'makeproduct': makeproduct})




    









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
