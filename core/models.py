from django.db import models
import uuid
import os
from django.db.models.signals import post_delete
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
        verbose_name_plural = "Informações"

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in a valid format.")

    about_me_image = models.ImageField(
        upload_to=settings_image, verbose_name='Imagem "sobre mim"', null=True)
    admin_name = models.CharField(max_length=50, null=True)
    admin_email = models.EmailField(max_length=255, null=True)
    admin_phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    admin_address = models.CharField(
        max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name='Descrição do negócio')

    def __str__(self):
        return 'Informações da empresa'


@receiver(post_delete, sender=Settings)
def delete_settings_image_file(sender, instance, **kwargs):
    instance.about_me_image.delete(False)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):

    position = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to=project_image)
    hover_image = models.ImageField(
        upload_to=project_image, null=True, blank=True)
    architects = models.CharField(
        max_length=255, verbose_name='Arquitectos', blank=True)
    area = models.DecimalField(
        max_digits=6, decimal_places=2, default=10, blank=True)
    year = models.CharField(
        max_length=20, verbose_name='Ano de construção', null=True, blank=True)
    construction = models.CharField(
        max_length=255, verbose_name='Construção', null=True, blank=True)
    state = models.CharField(
        max_length=255, verbose_name='Estado', null=True, blank=True)
    program = models.CharField(
        max_length=255, verbose_name='Programa', null=True, blank=True)
    client = models.CharField(
        max_length=255, verbose_name='Cliente', null=True, blank=True)
    location = models.CharField(
        max_length=255, verbose_name='Localização', null=True, blank=True)
    tipology = models.CharField(max_length=5, default="T0", blank=True)
    photographs = models.CharField(
        max_length=255, verbose_name='Fotógrafos', blank=True)
    engineering = models.CharField(
        max_length=255, verbose_name='Engenheiros', blank=True)
    images = models.CharField(
        max_length=255, verbose_name='Imagens', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="projects", blank=True)
    highlighted = models.BooleanField(default=False, verbose_name='Destacar')

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Project)
def delete_project_image_file(sender, instance, **kwargs):
    instance.main_image.delete(False)
    instance.hover_image.delete(False)


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


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    instance.image.delete(False)


class Partners(models.Model):
    class Meta:
        verbose_name_plural = "Parceiros"

    name = models.CharField(max_length=155, verbose_name='Nome da empresa')
    url = models.URLField(
        max_length=155, verbose_name='Site da empresa', blank=True)

    def __str__(self):
        return self.name
