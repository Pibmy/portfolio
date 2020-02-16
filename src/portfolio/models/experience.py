from django.db import models
from .skill import Skill
from .person import Person


class Formation(models.Model):

    # common fields
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()

    # relations
    skills = models.ManyToManyField(Skill, blank=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    diploma = models.CharField(max_length=30, blank=True)
    school = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{} - {}".format(self.school, self.diploma)


class Profesion(models.Model):

    # common fields
    description = models.TextField(blank=True)
    from_date = models.DateField()
    to_date = models.DateField()

    # relations
    skills = models.ManyToManyField(Skill, blank=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    job_label = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{} - {}".format(self.job_label, self.company)
