from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Education, Experience, Project, ProjectTag, SiteSettings, Skill


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('resume',)}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

admin.site.register(Experience, MarkdownxModelAdmin)
admin.site.register(ProjectTag)
admin.site.register(Skill)
admin.site.register(Education, MarkdownxModelAdmin)
admin.site.register(Project, MarkdownxModelAdmin)
