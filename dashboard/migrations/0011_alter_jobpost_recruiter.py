# Generated by Django 5.0.4 on 2024-05-07 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_recruiters_delete_customuser'),
        ('dashboard', '0010_alter_jobapplication_applydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='recruiter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.recruiters'),
        ),
    ]
