from django.contrib import admin

# Register your models here.
from myapp.models import *

class DetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(DetailsModel,DetailAdmin)

