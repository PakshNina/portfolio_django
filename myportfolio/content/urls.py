from .views import *
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles', ArticlesView.as_view(), name='articles'),
    path('documentation', DocumentationView.as_view(), name='documentation'),
    path('translations', TranslationsView.as_view(), name='translations'),
    path('presentations', PresentationsView.as_view(), name='presentations'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('conferences', ConferencesView.as_view(), name='conferences'),
    path('webinars', WebinarsView.as_view(), name='webinars'),
    path('projects', ProjectsView.as_view(), name='projects'),
]
