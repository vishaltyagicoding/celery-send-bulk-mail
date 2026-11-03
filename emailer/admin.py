from django.contrib import admin
from emailer.models import All_Mail

# Register your models here.
@admin.register(All_Mail)
class All_MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')