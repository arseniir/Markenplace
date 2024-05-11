from django.db import models

class MakeProductModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='ProjectA/images_products/')

    # def __self__(self):
    #     return f'{self.name}'

class CommentFeedbackModel(models.Model):
    cho = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))

    comment = models.TextField()
    feedback = models.IntegerField(choices=cho)