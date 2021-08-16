from django.contrib import admin
from .models import Dept,Doctor
# Register your models here.
admin.site.register(Dept)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','dept']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Doctor,DoctorAdmin)