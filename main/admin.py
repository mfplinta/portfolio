from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Education, Experience, Project, ProjectImage, ProjectTag, SiteSettings, Skill


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

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'alt_text', 'order')
    ordering = ('order', 'id')


@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    inlines = (ProjectImageInline,)
