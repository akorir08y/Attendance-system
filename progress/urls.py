"""progress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from progress import views 
from django.conf import settings
from django.conf.urls.static import static
from TTU_SYSTEM.views import student,lecturer

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('home/',include('home.urls', namespace='home')),
    path('attendance/',include('attendance.urls', namespace='attendance')),
    path('home1/',include('home1.urls', namespace='home1')),
    path('TTU_SYSTEM/',include('TTU_SYSTEM.urls',namespace='TTU_SYSTEM')),
    path('TTU_SYSTEM/register/student/', student.register, name='register'),
    path('TTU_SYSTEM/lec_register/lecturer/', lecturer.lec_register, name='lec_register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)