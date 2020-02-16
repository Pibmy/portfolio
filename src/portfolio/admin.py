from django.contrib import admin
from .models import Person, Skill, Formation, Profesion, Project

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    pass


@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
