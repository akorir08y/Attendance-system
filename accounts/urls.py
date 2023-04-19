from django.urls import path,include
from django.contrib.auth.views import (
    login,logout,password_reset,password_reset_done,
    password_reset_confirm,password_reset_complete)
from accounts import views

app_name='accounts'
urlpatterns = [
   
    path('reset-password', password_reset,{'template_name':'accounts/reset_password.html'}, name='password_reset'),
    path('reset-password/done',password_reset_done,{'template_name':'accounts/password_reset_done.html','post_reset_redirect':'accounts:password_reset_done'}, name='password_reset_done'), 
    path('reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>,+)',
     password_reset_confirm,{'template_name':'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),   
    path('reset-password/complete', password_reset_complete,{'template_name':'accounts/password_reset_complete.html'} ,name='password_reset_complete'),

]
