# Generated by Django 2.1.2 on 2019-07-10 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_auto_20190710_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlogs',
            name='network',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
