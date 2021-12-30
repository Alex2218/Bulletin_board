from django.contrib import admin
from .models import Bd, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd, BbAdmin)
admin.site.register(Rubric)
