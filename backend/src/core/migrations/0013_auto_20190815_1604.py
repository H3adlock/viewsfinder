# Generated by Django 2.2.3 on 2019-08-15 10:34

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190814_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]