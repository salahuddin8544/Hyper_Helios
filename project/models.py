from django.db import models
# Create your models here.
class inserting(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

