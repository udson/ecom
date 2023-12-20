from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
