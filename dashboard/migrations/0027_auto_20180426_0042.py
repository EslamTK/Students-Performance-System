# Generated by Django 2.0.4 on 2018-04-25 22:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0026_auto_20180425_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='absences',
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(93)]),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='failures',
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='final_grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True,
                                                   validators=[django.core.validators.MinValueValidator(0),
                                                               django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='midterm_grade',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0),
                                                               django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='prediction_grade',
            field=models.PositiveSmallIntegerField(editable=False, null=True,
                                                   validators=[django.core.validators.MinValueValidator(0),
                                                               django.core.validators.MaxValueValidator(100)]),
        ),
    ]