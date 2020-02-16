from django.db import models

from .skill import Skill
from .person import Person
from .experience import Formation, Profesion


class Project(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    from_date = models.DateField()
    to_date = models.DateField()

    # relations
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    skills = models.ManyToManyField(Skill, blank=True)
    pro_context = models.ForeignKey(
        Profesion,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    sch_context = models.ForeignKey(
        Formation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
