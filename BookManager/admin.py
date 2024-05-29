from django.contrib import admin
from BookManager.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

# Register your models here.
