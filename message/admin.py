from django.contrib import admin
from .models import Mymessages

# Register your models here.
class AdminMessage(admin.ModelAdmin):
    list_display = ('id', 'email', 'name','plocation','msg_date', 'agent_id')
    list_display_links = ('id', 'email')
    list_filter = ('agent_id','name')
    search_fields = ('agent_id',)
    list_per_page = 25

admin.site.register(Mymessages, AdminMessage)