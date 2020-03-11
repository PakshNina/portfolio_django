from django.db import models
from taggit.managers import TaggableManager
from single_instance_model.models import SingleInstanceModel


class Aboutme(models.Model, SingleInstanceModel):
    """About me content."""
    
    def __str__(self):
        return "Обо мне"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
    
    description = models.TextField(verbose_name='Описание', max_length=5000, blank=True, null=True)
    tags = TaggableManager()


class Documentation(models.Model):
    """Documentaion content."""
    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'

    title = models.CharField(verbose_name="Название", max_length=300)
    link_type = models.CharField(verbose_name="Тип ссылки", max_length=10)
    link = models.URLField(max_length=200)

class Articles(Documentation):
    """Articles content."""

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Translations(Documentation):
    """Translations content."""

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'


class Presentations(Documentation):
    """Presentations content."""

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'


class Courses(Documentation):
    """Courses content."""

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Conferences(Documentation):
    """Conferences content."""

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


class Webinars(Documentation):
    """Webinars content."""

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'

class Projects(Documentation):
    """Projects content."""

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'