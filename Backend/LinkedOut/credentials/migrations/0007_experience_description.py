# Generated by Django 4.1.7 on 2023-03-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0006_alter_applicant_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]