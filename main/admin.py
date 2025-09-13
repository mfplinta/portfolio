from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Experience, Skill, ProjectTag, Project, Education, BlogArticle

admin.site.register(Experience, MarkdownxModelAdmin)
admin.site.register(ProjectTag)
admin.site.register(Skill)
admin.site.register(Education, MarkdownxModelAdmin)
admin.site.register(Project, MarkdownxModelAdmin)
admin.site.register(BlogArticle, MarkdownxModelAdmin)