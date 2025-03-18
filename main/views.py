from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Project, Blog, Visitor
from django.db.models import Q
# Create your views here.


def index_view(request):
    user_profile = UserProfile.objects.first()

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    ip = get_ip(request=request)
    v = Visitor(visitor=ip)
    result = Visitor.objects.filter(Q(visitor__icontains=ip))
    
    if len(result) == 0:
        v.save()

    count = Visitor.objects.all().count()

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