from django.urls import path,include
from django.contrib.auth.views import (
    login,logout,password_reset,password_reset_done,
    password_reset_confirm,password_reset_complete)
from .views import student,lecturer,role

app_name='TTU_SYSTEM'
urlpatterns = [    
    path('login_success/', role.login_success, name='login_success'),

    path('lecturer/', include(([
        path('lec_register/', lecturer.lec_register, name='lec_register'),
        path('lec_login/',login, {'template_name':'TTU_SYSTEM/leclog.html'},name='lec_login'),
        path('lec_profile/', lecturer.lec_profile, name='lec_profile'),
        path('lec_profile/<id>/', lecturer.lec_profile_with_pk, name='lec_profile_with_pk'),
        path('profile/edit', lecturer.lec_edit_profile, name='lec_edit_profile'),
        path('lec_profileform/', lecturer.lec_profileform, name='lec_profileform'),
        path('lec_gallery', lecturer.lec_gallery, name='lec_gallery'),
        path('logout/',logout, {'template_name':'TTU_SYSTEM/logout.html'},name='logout'),
        path('change-password', lecturer.lec_change_password, name='lec_change_password'),path('reset-password', password_reset,{'template_name':'TTU_SYSTEM/reset_password.html','post_reset_redirect':'TTU_SYSTEM:password_reset_done'}, name='password_reset'),
        path('reset-password/done',password_reset_done,{'template_name':'TTU_SYSTEM/password_reset_done.html'}, name='password_reset_done'), 
        path('reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>,+)',
        password_reset_confirm,{'template_name':'TTU_SYSTEM/password_reset_confirm.html'}, name='password_reset_confirm'),   
        path('reset-password/complete', password_reset_complete,{'template_name':'TTU_SYSTEM/password_reset_complete.html'} ,name='password_reset_complete'),
        ]))),

    path('student/', include(([
        path('user_profileform/', student.user_profileform, name='user_profileform'),   
        path('login/',login, {'template_name':'TTU_SYSTEM/Stdlogin.html'},name='login'),
        path('logout/',logout, {'template_name':'TTU_SYSTEM/logout.html'},name='logout'),
        path('register/', student.register, name='register'),
        path('profile/', student.view_profile, name='view_profile'),
        path('profile/<id>/', student.view_profile_with_pk, name='view_profile_with_pk'),
        path('create_profile/', student.create_profile, name='create_profile'),
        path('gallery', student.gallery, name='gallery'),
        path('profile/edit', student.edit_profile, name='edit_profile'),
        path('change-password', student.change_password, name='change_password'),
        path('reset-password', password_reset,{'template_name':'TTU_SYSTEM/reset_password.html','post_reset_redirect':'TTU_SYSTEM:password_reset_done'}, name='password_reset'),
        path('reset-password/done',password_reset_done,{'template_name':'TTU_SYSTEM/password_reset_done.html'}, name='password_reset_done'), 
        path('reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>,+)',
        password_reset_confirm,{'template_name':'TTU_SYSTEM/password_reset_confirm.html'}, name='password_reset_confirm'),   
        path('reset-password/complete', password_reset_complete,{'template_name':'TTU_SYSTEM/password_reset_complete.html'} ,name='password_reset_complete'),
    ])))
]

