from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from ProjectB.views import show_products, MakeProduct, all_products, UpdateDeleteProduct, DeleteProductView, CreateComment


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.products_url = reverse('products')
        self.make_products_url = reverse('make_products')
        self.update_product_id_url = reverse('update_product_id')

        # self.update_products_url = reverse('update_products')
        # self.product_id = 27  
        # self.update_products_url = reverse('update_product', args=[self.product_id])
        
        # self.delete_product_id_url = reverse('delete_product_id')
        self.comment_url = reverse('comment')
        self.user = User.objects.create_user(username='krasavchic', email='IadoreDjango@gmail.com', password='django1234')
    
    
    def test_show_products(self):
        request = self.factory.get(self.products_url)
        request.user = self.user
        response = show_products(request)
        self.assertEqual(response.status_code, 200)



    def test_MakeProduct_get(self):
        data = {'id': 27, 'name': 'Popit', 'description': 'He  and smart', 'category': 'Drugs', 'price': 178, 'photo': 'http://localhost:8000/ProjectA/images_products/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA_%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_%D0%B7_2024-04-22_16-25-04_L6bTtlF.png'}
        request = self.factory.post(self.make_products_url, data)
        request.user = self.user
        response = MakeProduct.as_view()(request)
        self.assertEqual(response.status_code, 200)


    # def test_all_products(self):
    #     request = self.factory.get(self.update_product_id_url)
    #     request.user = self.user
    #     response = all_products(request)
    #     self.assertEqual(response.status_code, 200)


    # def test_UpdateDeleteProduct(self):
    #     data = {'id': 27, 'name': 'Popit', 'description': 'He  and smart', 'category': 'Drugs', 'price': 1, 'photo': 'http://localhost:8000/ProjectA/images_products/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA_%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_%D0%B7_2024-04-22_16-25-04_L6bTtlF.png'}
    #     request = self.factory.put(self.update_products_url, data)
    #     request.user = self.user
    #     response = UpdateDeleteProduct.as_view()(request, product_id=self.product_id)
    #     self.assertEqual(response.status_code, 200)

    # def test_UpdateDeleteProduct(self):
    #     data = {'id': 27, 'name': 'Popit', 'description': 'He  and smart', 'category': 'Drugs', 'price': 1, 'photo': 'http://localhost:8000/ProjectA/images_products/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA_%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_%D0%B7_2024-04-22_16-25-04_L6bTtlF.png'}
    #     request = self.factory.delete(self.delete_product_id_url, data)
    #     request.user = self.user
    #     response = DeleteProductView.as_view()(request, product_id=self.product_id)
    #     self.assertEqual(response.status_code, 204)

    # def test_CreateComment(self):
    #     data = {'comment': 'Guys you are the best', 'feedback': '5'}
    #     request = self.factory.post(self.comment_url, data)
    #     request.user = self.user
    #     response = CreateComment.as_view()(request)
    #     self.assertEqual(response.status_code, 200)

