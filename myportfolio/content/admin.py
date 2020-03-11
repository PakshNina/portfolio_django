from django.contrib import admin
from content.models import * 
from single_instance_model.admin import SingleInstanceModelAdmin


# Register your models here.
@admin.register(Aboutme)
class AboutUsAdmin(SingleInstanceModelAdmin):
    pass

admin.site.register(Documentation)
admin.site.register(Articles)
admin.site.register(Translations)
admin.site.register(Presentations)
admin.site.register(Courses)
admin.site.register(Conferences)
admin.site.register(Webinars)
admin.site.register(Projects)
