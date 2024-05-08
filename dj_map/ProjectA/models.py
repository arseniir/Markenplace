from django.db import models

class MakeProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='ProjectA/images_products/')

    # def __self__(self):
    #     return f'{self.name}'

class CommentFeedbackModel(models.Model):
    comment = models.TextField()
    cho = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    feedback = models.IntegerField(choices=cho)