# Generated by Django 2.0.2 on 2018-03-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0004_educator_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='educator',
            name='image_url',
            field=models.CharField(default='hkjdada', max_length=200),
            preserve_default=False,
        ),
    ]
