# Generated by Django 4.1.7 on 2023-03-30 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0007_experience_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='position',
            new_name='title',
        ),
    ]
