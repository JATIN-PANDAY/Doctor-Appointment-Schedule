from django.contrib import admin
from myapp.models import Doctor
from myapp.models import Patient
from myapp.models import MasterTable




# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MasterTable)

