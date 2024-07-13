from django.db import models

# Create your models here.

class Book(models.Model):
    book_name_th = models.CharField(max_length=100)
    book_name_en = models.CharField(max_length=100)
    number_si = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    detail_book = models.CharField(max_length=100)
    BOOKSHOP_CHOICES = [
        ("B2S","B2S"),
        ("Inthon","Inthon"),
        ("Se-ed","Se-ed"),
        ("Meb","Meb"),
        
       
    ];
    bookshop = models.CharField(
        max_length=20,
        choices=BOOKSHOP_CHOICES,
        default="B2S"
    )
    sale_book = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
