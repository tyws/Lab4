from django.db import models

# Create your models here.

class Book(models.Model):
    ISBN = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=30)
    AuthorID = models.IntegerField()
    Publisher = models.CharField(max_length=50)
    PublishDate = models.CharField(max_length=30)
    Price = models.FloatField()

class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Country = models.CharField(max_length=30)

