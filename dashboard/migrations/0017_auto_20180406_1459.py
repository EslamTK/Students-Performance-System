# Generated by Django 2.0.2 on 2018-04-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0016_auto_20180406_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='absences',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='failures',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='final_grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='midterm_grade',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='prediction_grade',
            field=models.PositiveSmallIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='study_time',
            field=models.PositiveSmallIntegerField(),
        ),
    ]