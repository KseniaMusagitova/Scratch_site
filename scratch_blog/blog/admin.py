from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class ProgramInline(admin.StackedInline):
    model = models.Program
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_at', 'id']
    inlines = [ProgramInline]


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
