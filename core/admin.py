from django.contrib import admin
from core import models


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.Projects, ProjectsAdmin)
