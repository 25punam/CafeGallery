# Generated by Django 4.2.6 on 2023-10-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_cafemodel_remove_menumodel_img_menumodel_cafe'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafemodel',
            name='opening_hours',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='cafemodel',
            name='opening_time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]