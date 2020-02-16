from django.db import models
from .skill import Skill


class Person(models.Model):

    # basic info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30, blank=True)
    localisation = models.CharField(max_length=2, default='fr')

    # personal info use with care
    email = models.EmailField(max_length=256, unique=True)
    address = models.CharField(max_length=128, blank=True)
    # phone = models.CharField(max_lenght=30, blank=True)

    # optional info
    description = models.TextField(blank=True)
    interests = models.TextField(blank=True)

    ###
    # Methods
    ###

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_human_skills(self):
        return [s for s in self.skills if s.kind == 0]

    def get_tech_skills(self):
        return [s for s in self.skills if s.kind == 1]

    ###
    # Properties
    ###

    _projects = None
    _profesions = None
    _formations = None
    _skills = None

    @property
    def projects(self):
        if self._projects is None:
            self._projects = self.project_set.all()
        return self._projects

    @property
    def profesions(self):
        if self._profesions is None:
            self._profesions = self.profesion_set.all()
        return self._profesions

    @property
    def formations(self):
        if self._formations is None:
            self._formations = self.formation_set.all()
        return self._formations

    @property
    def skills(self):
        if self._skills is None:
            query = (
                "SELECT * FROM portfolio_skill "
                "WHERE id IN ( "
                "    SELECT skill_id FROM portfolio_project_skills "
                "    WHERE project_id IN ( "
                "        SELECT id FROM portfolio_project "
                "        WHERE person_id = %s "
                "    ) "
                "    UNION "
                "    SELECT skill_id FROM portfolio_formation_skills "
                "    WHERE formation_id IN ( "
                "        SELECT id FROM portfolio_formation "
                "        WHERE person_id = %s "
                "    ) "
                "    UNION "
                "    SELECT skill_id FROM portfolio_profesion_skills "
                "    WHERE profesion_id IN ( "
                "        SELECT id FROM portfolio_profesion "
                "        WHERE person_id = %s "
                "    ) "
                ")"
            )
            self._skills = Skill.objects.raw(query, [self.id] * 3)
        return self._skills
