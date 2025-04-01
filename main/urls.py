from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('projects/', project_list_view, name='projects_list'),
    path('projects/<slug:slug>/', project_details_view, name='project_detail'),
    path('blogs/', blogs_list_view, name='blogs_list'),
    path('blogs/<slug:slug>/', blog_details_view, name='blog_detail'),
    path('star_system_simulation/', star_system_simulation_view, name='star_system_simulation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
