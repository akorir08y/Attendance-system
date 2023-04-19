from django.urls import path
from home1.views import HomeView1
from . import views

app_name='home1'
urlpatterns = [
    path('', HomeView1.as_view(), name='home1'),
    path('connect/<operation>,+/<id>/', views.change_friend, name='change_friend'),
    ]