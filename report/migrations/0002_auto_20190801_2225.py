# Generated by Django 2.2.3 on 2019-08-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='char',
            field=models.CharField(blank=True, default=None, max_length=20),
            preserve_default=False,
        ),
    ]