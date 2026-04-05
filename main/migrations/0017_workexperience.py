# Generated manually for WorkExperience model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('role', models.CharField(max_length=200)),
                ('duration', models.CharField(help_text='e.g. Summer 2024 or Jan 2023 – Aug 2023', max_length=120)),
                ('location', models.CharField(max_length=200)),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'work experiences',
                'ordering': ['sort_order', '-id'],
            },
        ),
    ]
