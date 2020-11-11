from django.contrib import admin
from .models import Createlogs, TblBranchCompDept, TblInternet, TblJobTitle, TblJobTitle, TblTransactionType

admin.site.register(Createlogs)
admin.site.register(TblBranchCompDept)
admin.site.register(TblInternet)
admin.site.register(TblJobTitle)
admin.site.register(TblTransactionType)