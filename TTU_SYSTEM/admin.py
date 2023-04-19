from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from TTU_SYSTEM.forms import StdRegForm,LecRegForm,EditProfileForm,EditProfileForm1
from TTU_SYSTEM.models import CustomUser,LecProfile,UserProfile


class ProfileInline(admin.StackedInline):
    model = LecProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class ProfileInline1(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,ProfileInline1)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_Employee_no','get_reg_no')
    list_select_related = ('user_profile','lec_profile' )

    def get_Employee_no(self, instance):
        return instance.lec_profile.Employee_no
    get_Employee_no.short_description = 'Emp_no'

    def get_reg_no(self, instance):
        return instance.user_profile.reg_no
    get_reg_no.short_description = 'reg_no'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(LecProfile)
admin.site.register(UserProfile)
