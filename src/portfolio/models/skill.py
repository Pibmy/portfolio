from django.db import models


class Skill(models.Model):

    KINDS = ((0, 'Human Skill'), (1, 'Tech. Skill'))

    name = models.CharField(max_length=30)
    kind = models.IntegerField(choices=KINDS)

    # optional
    icon = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
