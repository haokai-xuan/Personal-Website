from django.urls import path
from .views import index_view, contact_view, project_list_view, project_details_view, blogs_list_view, blog_details_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('projects/', project_list_view, name='projects_list'),
    path('projects/<slug:slug>/', project_details_view, name='project_detail'),
    path('blogs/', blogs_list_view, name='blogs_list'),
    path('blogs/<slug:slug>/', blog_details_view, name='blog_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
