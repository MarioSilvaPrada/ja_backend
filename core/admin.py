from django.contrib import admin
from core import models

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Project, ProjectsAdmin)
admin.site.register(models.Partners)
admin.site.register(models.About)
admin.site.register(models.Settings)