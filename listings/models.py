from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Category(models.Model):
    categoryID = models.AutoField(null=False , primary_key=True)
    categoryName = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    def __int__(self):
        return self.categoryID

    def __str__(self):
        return self.categoryName


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    category_ID = models.ForeignKey(Category  , on_delete=models.CASCADE)
    product_no = models.IntegerField()
    title = models.CharField(max_length = 200)
    companyName = models.CharField(max_length=200 , null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    unit_in_stock = models.PositiveIntegerField(default=0)
    discounts = models.DecimalField(max_digits=7 , decimal_places=4)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        return self.title
    
