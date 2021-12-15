from django.contrib import admin
from .models import UserAccount
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UserAccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name_plural = 'user account'

class UserAdmin(BaseUserAdmin):
    inlines = (UserAccountInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(UserAccount)

# Register your models here.
