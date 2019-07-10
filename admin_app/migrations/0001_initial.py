# Generated by Django 2.1.2 on 2019-07-10 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Createlogs',
            fields=[
                ('logsid', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('transactiontype', models.CharField(blank=True, max_length=50, null=True)),
                ('network', models.CharField(blank=True, max_length=20, null=True)),
                ('jabber', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('internet', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('work_order', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'admin_app_createlogs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('logsid', models.AutoField(db_column='logsID', primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(db_column='Date', default=django.utils.timezone.now)),
                ('transactiontype', models.CharField(db_column='TransactionType', max_length=50)),
                ('branch', models.CharField(db_column='Branch', max_length=100)),
                ('company', models.CharField(db_column='Company', max_length=100)),
                ('department', models.CharField(db_column='Department', max_length=100)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('transaction', models.CharField(db_column='Transaction', max_length=50)),
                ('account', models.CharField(db_column='Account', max_length=100)),
                ('remarks', models.TextField(db_column='Remarks')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='logsnew',
            fields=[
                ('logsid', models.AutoField(db_column='logsID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='Date', default=django.utils.timezone.now)),
                ('transactiontype', models.CharField(db_column='TransactionType', max_length=50)),
                ('branch', models.CharField(db_column='Branch', max_length=100)),
                ('company', models.CharField(db_column='Company', max_length=100)),
                ('department', models.CharField(db_column='Department', max_length=100)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('transaction', models.CharField(db_column='Transaction', max_length=50)),
                ('account', models.CharField(db_column='Account', max_length=100)),
                ('remarks', models.TextField(db_column='Remarks')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
