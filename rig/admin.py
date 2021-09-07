from django.contrib import admin
from .models import Event,Categories
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Event,EventAdmin)
admin.site.register(Categories)