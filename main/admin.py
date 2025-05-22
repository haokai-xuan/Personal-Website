from django.contrib import admin
from .models import UserProfile, Tag, Project, MediaFile, Blog

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(MediaFile)
admin.site.register(Blog)