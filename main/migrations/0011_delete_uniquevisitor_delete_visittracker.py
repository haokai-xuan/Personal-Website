# Generated by Django 5.1.1 on 2025-03-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_visittracker_uniquevisitor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UniqueVisitor',
        ),
        migrations.DeleteModel(
            name='VisitTracker',
        ),
    ]
