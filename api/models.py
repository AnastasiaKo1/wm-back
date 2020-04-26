from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=1000)
    text = models.TextField()



    