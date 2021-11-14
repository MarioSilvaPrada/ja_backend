from django.contrib import admin
from core import models


class SectionInline(admin.StackedInline):
    model = models.ProjectSection
    ordering = ()
    extra = 0


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'highlighted']
    inlines = [SectionInline]
    ordering = ('position',)


class ImagesInline(admin.StackedInline):
    model = models.Image
    ordering = ()
    extra = 0


class ProjectsSectionAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    ordering = ('project', 'section_name')


admin.site.register(models.Project, ProjectsAdmin)
admin.site.register(models.ProjectSection, ProjectsSectionAdmin)
admin.site.register(models.Image)
admin.site.register(models.Partners)
admin.site.register(models.Settings)
admin.site.register(models.Tag)
