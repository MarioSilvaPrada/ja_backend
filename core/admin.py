from django.contrib import admin
from core import models


class SectionInline(admin.StackedInline):
    model = models.ProjectSection
    ordering = ()
    extra = 0


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [SectionInline]


class ImagesInline(admin.StackedInline):
    model = models.Image
    ordering = ()
    extra = 0


class ProjectsSectionAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    ordering = ('project', 'section_name')


class ImagesAdmin(admin.ModelAdmin):

    actions = ['delete_selected']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            print('iamgem', obj)


admin.site.register(models.Project, ProjectsAdmin)
admin.site.register(models.ProjectSection, ProjectsSectionAdmin)
admin.site.register(models.Image, ImagesAdmin)
admin.site.register(models.Partners)
admin.site.register(models.About)
admin.site.register(models.Settings)
