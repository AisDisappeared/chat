from django.contrib import admin
from .models import * 


class ChatGroupAdmin(admin.ModelAdmin):
    search_fields = ['group_name']
    list_display = ['group_name']
    list_filter = ['group_name']
    save_as = True 
    save_on_top = True 



class GroupMessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ['author','created_at','group']
    list_filter = ['author','group']
    search_fields = ['group']


admin.site.register(ChatGroup,ChatGroupAdmin)
admin.site.register(GroupMessage,GroupMessageAdmin)