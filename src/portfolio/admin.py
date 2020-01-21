from django.contrib import admin
from .models import Person, Project, Skill, XP

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(XP)
class XPAdmin(admin.ModelAdmin):
    pass
