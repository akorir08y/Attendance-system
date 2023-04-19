from django.db import models
from TTU_SYSTEM.models import CustomUser
from django.contrib.auth.models import Group

# Create your models here.
class Post2(models.Model):
    title = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

class UserGroup(models.Model):
    group = models.OneToOneField(Group,on_delete=models.CASCADE,null=True)
    users = models.ManyToManyField(CustomUser) 
    current_user1 = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Owner2',null=True)      

    @classmethod
    def add_to_group(cls,current_user1,new_group_member):
        usergroup, created = cls.objects.get_or_create(current_user1=current_user)
        usergroup.users.add(new_group_member)

    @classmethod
    def remove_from_group(cls,current_user1,new_group_member):
        friend, remove = cls.objects.get_or_create(current_user1=current_user)
        friend.users.remove(remove_group_member) 
