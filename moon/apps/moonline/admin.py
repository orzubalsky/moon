from moonline.models import *
from django.contrib import admin

class StoryAdmin(admin.ModelAdmin):
    list_display        = ('short_content', 'on_days',)

admin.site.register(Story, StoryAdmin)
admin.site.register(MoonDay)
