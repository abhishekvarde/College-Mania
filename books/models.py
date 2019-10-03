from django.db import models

# Create your models here.


class Ad(models.Model):
    product_id = models.AutoField
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    des = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/images')
    contact_no = models.CharField(max_length=14, default="")
    address = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.name
