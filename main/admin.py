from django.contrib import admin
from .models import UserProfile, Tag, Project, MediaFile, Blog, WorkExperience

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(MediaFile)
admin.site.register(Blog)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'role', 'duration', 'location', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('company_name', 'role', 'location')