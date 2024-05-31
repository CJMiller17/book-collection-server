from django.contrib import admin
from BookManager.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

My_Models = [Profile, Book]
admin.site.register(My_Models, ProfileAdmin)

# Register your models here.
