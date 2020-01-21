from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def all_skills(request):
    return HttpResponse("All skills")


def skill(request, id):
    return HttpResponse("Skill N°: {}".format(id))


def all_projects(request):
    return HttpResponse("All projects")


def project(request, id):
    return HttpResponse("Project N°: {}".format(id))
