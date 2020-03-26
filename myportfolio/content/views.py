from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
from abc import abstractproperty
from . import urls
from  django.views.generic.base import ContextMixin
from abc import abstractproperty
from taggit.models import Tag


class Link:
    pass


class LinkNameMixin(ContextMixin):
    titles = {
            'index': 'Обо мне',
            'articles': 'Статьи',
            'documentation':'Документация',
            'translations':'Переводы',
            'presentations':'Презентации',
            'courses':'Курсы',
            'conferences':'Конференции',
            'webinars':'Вебинары',
            'projects':'Проекты',
        }
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_links = []
        class_name = self.__class__.__name__

        for url in urls.urlpatterns:
            link = Link()
            link.name = url.name
            link.title = self.titles.get(link.name)
            link.style_class = ''
            if link.name in class_name.lower():
                link.style_class = 'activated'
                context['header'] = self.titles.get(link.name)
            all_links.append(link)
        context['all_links'] = all_links
        context['all_tags'] = Tag.objects.all()

        return context


class IndexView(LinkNameMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutme'] = Aboutme.objects.first()
      
        return context


class CustomBaseView(LinkNameMixin, TemplateView):
    template_name = "info_view.html"
    
    @abstractproperty
    def models_objects(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.models_objects
        return context


class ArticlesView(CustomBaseView):
    @property
    def models_objects(self):
        return Articles.objects.all()


class DocumentationView(CustomBaseView):
    @property
    def models_objects(self):
        return Documentation.objects.all()


class TranslationsView(CustomBaseView):
    @property
    def models_objects(self):
        return Translations.objects.all()


class PresentationsView(CustomBaseView):
    @property
    def models_objects(self):
        return Presentations.objects.all()


class CoursesView(CustomBaseView):
    @property
    def models_objects(self):
        return Courses.objects.all()


class ConferencesView(CustomBaseView):
    @property
    def models_objects(self):
        return Conferences.objects.all()


class WebinarsView(CustomBaseView):
    @property
    def models_objects(self):
        return Webinars.objects.all()


class ProjectsView(CustomBaseView):
    @property
    def models_objects(self):
        return Projects.objects.all()


class TagView(CustomBaseView):
    @property
    def models_objects(self):
        return Tag.objects.all()

