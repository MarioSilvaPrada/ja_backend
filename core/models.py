from django.db import models
import uuid
import os
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from django.core.validators import RegexValidator


def settings_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/site_settings/', filename)


def project_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/projects/', filename)


class Settings(models.Model):
    class Meta:
        verbose_name_plural = "Definições"

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in a valid format.")

    main_background_image = models.ImageField(upload_to=settings_image)
    admin_name = models.CharField(max_length=50, unique=True, null=True)
    admin_email = models.EmailField(max_length=255, unique=True, null=True)
    admin_phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    admin_address = models.CharField(
        max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return 'My Settings'


class Project(models.Model):

    name = models.CharField(max_length=255)
    main_image = models.ImageField(null=True, upload_to=project_image)

    def __str__(self):
        return self.name


class ProjectSection(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='section',
        on_delete=models.CASCADE,
    )
    section_name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.project.name} {self.section_name}'


class Image(models.Model):
    section = models.ForeignKey(
        ProjectSection,
        related_name='image',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=project_image)
    image_name = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return self.image_name or f'imagem - {self.section}'


class About(models.Model):
    class Meta:
        verbose_name_plural = "Sobre"

    description = models.TextField(verbose_name='Descrição do negócio')
    services = models.CharField(max_length=255, verbose_name='Serviços')


class Partners(models.Model):
    class Meta:
        verbose_name_plural = "Parceiros"

    name = models.CharField(max_length=155, verbose_name='Nome da empresa')
    url = models.URLField(
        max_length=155, verbose_name='Site da empresa', blank=True)



def delete_from_s3(bucket, model, aws_secret, aws_key):
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=aws_key, aws_secret_access_key=aws_secret
        )
        s3.delete_object(Bucket=bucket, Key=model)
        return True
    except Exception as ex:
        print(str(ex))
        return False

