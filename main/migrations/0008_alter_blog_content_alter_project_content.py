# Generated by Django 5.1.1 on 2024-10-02 23:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
