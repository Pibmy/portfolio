from django.shortcuts import render
from django.http import HttpResponse

from .models import Person


def index(request):
    user = Person.objects.get(id=1)
    return render(request, 'index.html', context={'user': user})


def all_skills(request):
    return HttpResponse("All skills")


def skill(request, id):
    return HttpResponse("Skill N°: {}".format(id))


def all_projects(request):
    return HttpResponse("All projects")


def project(request, id):
    return HttpResponse("Project N°: {}".format(id))
