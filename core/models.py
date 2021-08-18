from django.db import models
import uuid
import os
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver




def settings_image(instance, filename):
    print('inst', instance)
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/site_settings/', filename)


class Settings(models.Model):
    class Meta:
        verbose_name_plural = "Settings"

    main_background_image = models.ImageField(upload_to=settings_image)

    def __str__(self):
        return 'My Settings'


class Project(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name



def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)

@receiver(pre_delete, sender=Settings)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance.main_background_image:
        _delete_file(instance.main_background_image.path)
