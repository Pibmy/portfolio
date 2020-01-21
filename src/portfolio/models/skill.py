from django.db import models


class Skill(models.Model):

    CATEGORIES = (
        ('IT-L', 'Langage de programation'),
        ('IT-T', 'Outils de programation'),
        ('IT-S', 'Systèmes Informatique'),
        ('FH', 'Humaine'),
        ('O', 'Other'),
    )

    category = models.CharField(max_length=30, choices=CATEGORIES)
    name = models.CharField(max_length=30)

    # optional
    icon = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
