# Generated by Django 2.1.2 on 2019-07-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0010_auto_20190710_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlogs',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='createlogs',
            name='jabber',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='createlogs',
            name='job_title',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='createlogs',
            name='network',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]
