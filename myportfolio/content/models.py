from django.db import models
from taggit.managers import TaggableManager
from single_instance_model.models import SingleInstanceModel
from abc import ABCMeta
import re
from martor.models import MartorField
from taggit.models import Tag
from .mycode import transliterate


class Aboutme(models.Model, SingleInstanceModel):
    """About me content."""
    
    def __str__(self):
        return "Обо мне"

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
    
    description = MartorField(verbose_name='Описание', max_length=5000, blank=True, null=True)

    def description_as_list(self):
        return self.description.split('\n')


class CustomBaseModel(models.Model):

    class Meta:
        abstract = True

    """Base model for class creation."""
    title = models.CharField(verbose_name="Название", max_length=300)
    link_type = models.CharField(verbose_name="Тип ссылки", max_length=10)
    link = models.URLField(max_length=200, verbose_name="Ссылка на элемент")
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Documentation(CustomBaseModel):
    """Documentaion content."""

    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'


class Articles(CustomBaseModel):
    """Articles content."""

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Translations(CustomBaseModel):
    """Translations content."""

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'


class Presentations(CustomBaseModel):
    """Presentations content."""

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'


class Courses(CustomBaseModel):
    """Courses content."""

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Conferences(CustomBaseModel):
    """Conferences content."""

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


class Webinars(CustomBaseModel):
    """Webinars content."""

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'


class Projects(CustomBaseModel):
    """Projects content."""

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'