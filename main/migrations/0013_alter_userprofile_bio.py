# Generated by Django 5.1.1 on 2025-03-25 21:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
