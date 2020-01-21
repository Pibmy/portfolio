from django.db import models


class Person(models.Model):

    # basic info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30, blank=True)

    # localisation info
    localisation = models.CharField(max_length=2, default='fr')

    # personal info use with care
    email = models.EmailField(max_length=256, unique=True)
    # phone = models.CharField(max_lenght=30, blank=True)
    address = models.CharField(max_length=128, blank=True)

    # optional innfo
    description = models.TextField(blank=True)

    # interests
    interests = models.TextField(blank=True)
