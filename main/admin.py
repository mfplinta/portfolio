from django.contrib import admin

from .models import Experience, Skill, ProjectTag, Project, Education

admin.site.register(Experience)
admin.site.register(ProjectTag)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)