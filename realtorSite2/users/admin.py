from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from users.models import NewUser


class UserAdminDisplay(UserAdmin):
    list_display=('email','user_name','is_staff','is_superuser')
    ordering=('-start_date',)
    search_fields=('email','user_name',)
    list_filter=('email','user_name',)
    fieldsets=(( None,{'fields':('email','user_name','first_name','last_name','password')}  ),
               ('permission',{"fields":('is_staff','is_superuser',)}  ),
               )
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    
admin.site.register(NewUser,UserAdminDisplay)
    