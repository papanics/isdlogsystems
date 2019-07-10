from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Logs(models.Model):
    logsid = models.AutoField(db_column='logsID', primary_key=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date', default=timezone.now )  # Field name made lowercase.
    transactiontype = models.CharField(db_column='TransactionType', max_length=50)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=100)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    transaction = models.CharField(db_column='Transaction', max_length=50)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=100)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks')  # Field name made lowercase.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    

  
    
    def __str__(self):
        return self.name

class logsnew(models.Model):
    logsid = models.AutoField(db_column='logsID', primary_key=True)
    date = models.DateTimeField(db_column='Date', default=timezone.now)
    transactiontype = models.CharField(db_column='TransactionType', max_length=50)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=100)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    transaction = models.CharField(db_column='Transaction', max_length=50)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=100)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks')  # Field name made lowercase.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Createlogs(models.Model):
    logsid = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, blank=True)
    transactiontype = models.CharField(max_length=50, null=True)
    network = models.CharField(max_length=20, blank=True)
    jabber = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    internet = models.CharField(max_length=20, null=True,  default="None")
    description = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(null=True, default="New Account") 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    work_order = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'admin_app_createlogs'

    def get_absolute_url(self):
        return reverse('admin_app:logs-detail', kwargs={'pk': self.pk})





    
  