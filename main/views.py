from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Project, Blog
# Create your views here.


def index_view(request):
    user_profile = UserProfile.objects.first()
    return render(request, 'main/index.html', {'user_profile': user_profile})


def contact_view(request):
    return render(request, 'main/contact.html')


def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'main/projects_list.html', {'projects': projects})


def project_details_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})


def blogs_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogs_list.html', {'blogs': blogs})


def blog_details_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'main/blog_detail.html', {'blog': blog})

def handle_404(request, exception):
    return render(request, "main/404.html", {})