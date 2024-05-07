# Generated by Django 5.0.4 on 2024-05-07 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='JobpostId',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='UserApplied',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='jobpost',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jobpost'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.userprofile'),
        ),
    ]
