from django.db import models


class XP(models.Model):

    job = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    is_scolarship = models.BooleanField(default=False)

    from_date = models.DateField()
    to_date = models.DateField()

    description = models.TextField(blank=True)
