from django.db import models
from TTU_SYSTEM.models import CustomUser
from django.utils import timezone

import pytz

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
class Friends(models.Model):
    users = models.ManyToManyField(CustomUser)  
    current_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='owner',null=True)


    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend, remove = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(remove_friend)


