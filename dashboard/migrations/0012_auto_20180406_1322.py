# Generated by Django 2.0.2 on 2018-04-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0011_studentcourse_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
