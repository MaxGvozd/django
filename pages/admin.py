from django.contrib import admin
from pages.models import ModelFirst


# Register your models here.
@admin.register(ModelFirst)
class ModelNameAdmin(admin.ModelAdmin):
    pass
