# Generated by Django 2.1.2 on 2019-07-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_auto_20190710_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlogs',
            name='company',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='createlogs',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
