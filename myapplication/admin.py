from django.contrib import admin
from . models import DataForm
# Register your models here.
@admin.register(DataForm)

class UserAdmin(admin.ModelAdmin):
    list_display=('id','Date','Sizeofcontainer','From','To','Customer','Carriedby','Diesel','Price','Status')