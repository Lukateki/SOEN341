# Generated by Django 4.1.7 on 2023-03-04 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0018_remove_candidateconfig_candidate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='candidate',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='candidate',
            new_name='applicant',
        ),
    ]