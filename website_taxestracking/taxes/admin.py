from django.contrib import admin
from taxes.models import *


@admin.register(taxesModel)
class taxesAdmin(admin.ModelAdmin):
    pass


@admin.register(taxNameModel)
class taxesAdmin(admin.ModelAdmin):
    pass
