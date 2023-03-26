# Generated by Django 4.1.7 on 2023-03-23 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
        ('JobListings', '0003_rename_jobapplicatons_jobapplications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobListings.job')),
            ],
        ),
        migrations.DeleteModel(
            name='JobApplications',
        ),
    ]