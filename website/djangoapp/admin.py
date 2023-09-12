from django.contrib import admin
from .models import Member # name of model

# Register your models here.
class MemberAdmin(admin.ModelAdmin): # set list_display to display fields in admin page
    list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)