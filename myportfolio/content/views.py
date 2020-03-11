from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutme'] = Aboutme.objects.first()
        return context

class ArticlesView(TemplateView):
    template_name = "articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Articles.objects.first()
        return context

class DocumentationView(TemplateView):
    template_name = "documentation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documentation'] = Documentation.objects.first()
        return context

class TranslationsView(TemplateView):
    template_name = "translations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['translations'] = Translations.objects.first()
        return context


class PresentationsView(TemplateView):
    template_name = "presentations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['presentations'] = Presentations.objects.first()
        return context


class CoursesView(TemplateView):
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.first()
        return context


class ConferencesView(TemplateView):
    template_name = "conferences.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conferences'] = Conferences.objects.first()
        return context

class WebinarsView(TemplateView):
    template_name = "webinars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['webinars'] = Webinars.objects.first()
        return context

class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Projects.objects.first()
        return context

# classes_name = ['Articles', 'Documentation']

# class MetaView(type):
#     def __init__(cls, name, bases, attrs):
#         super().__init__(name,bases, attrs)

# view_classes = []
# for name in classes_name:
#     view_classes.appesnd(
#         MetaView(
#             name,
#             (TemplateView,),
#             {   
#                 'name': name.lower(),
#                 'template_name': "{0}.html".format(name.lower()),
#             }
#         )
#     )
