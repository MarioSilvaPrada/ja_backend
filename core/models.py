from django.db import models
import os

def settings_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/site_settings/', filename)

class Settings(models.Model):
    class Meta:
        verbose_name_plural = "Settings"

    main_background_image = models.ImageField(upload_to=settings_image)


class Project(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
