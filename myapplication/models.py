from django.db import models

# Create your models here.
class DataForm(models.Model):
    Date=models.DateField()
    Sizeofcontainer=models.CharField(max_length=155)
    From=models.CharField(max_length=155)
    To=models.CharField(max_length=155)
    Customer=models.CharField(max_length=155)
    Carriedby=models.CharField(max_length=155)
    Diesel=models.CharField(max_length=155)
    Price=models.CharField(max_length=155)
    Status=models.CharField(max_length=155)
    




