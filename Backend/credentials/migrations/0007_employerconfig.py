# Generated by Django 4.1.7 on 2023-02-17 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0006_alter_candidateconfig_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=1500)),
                ('headquarters', models.CharField(max_length=100)),
                ('employer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credentials.employer')),
            ],
        ),
    ]
