from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateTimeField()
    Ite_exists = models.BooleanField()
    slug = models.SlugField()