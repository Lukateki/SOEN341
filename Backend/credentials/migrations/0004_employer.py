# Generated by Django 4.1.7 on 2023-02-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]