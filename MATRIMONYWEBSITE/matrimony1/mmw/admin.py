from django.contrib import admin
from .models import personinfo
# Register your models here.
@admin.register(personinfo)
class admininfoperson(admin.ModelAdmin):
    list_display=['name','email','gender','date','religion','city','age','physical_disability','education','occupation','img','biodata']
    
