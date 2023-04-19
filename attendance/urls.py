from django.urls import path
from attendance.views import GroupView1
from . import views

app_name='attendance'
urlpatterns = [
    path('', GroupView1.as_view(), name='group'),
    path('connect/<operation>,+/<id>/', views.group1, name='group1'),
    ]