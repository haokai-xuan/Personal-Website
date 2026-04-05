from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cv = models.FileField(upload_to='cvs/')
    bio = RichTextField()
    title = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    content = RichTextField()
    date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']  # Sort by most recent

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MediaFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    content = RichTextField()
    date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']  # Sort by most recent

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    """Past internship / work entries shown on the home page."""

    company_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos/')
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=120, help_text='e.g. Summer 2024 or Jan 2023 – Aug 2023')
    location = models.CharField(max_length=200)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', '-id']
        verbose_name_plural = 'work experiences'

    def __str__(self):
        return f'{self.role} @ {self.company_name}'

