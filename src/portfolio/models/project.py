from django.db import models


class Project(models.Model):

    name = models.CharField(max_length=30)

    date = models.DateField()
    duration = models.DurationField(blank=True)

    company = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
