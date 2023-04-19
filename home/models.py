from django.db import models
from TTU_SYSTEM.models import CustomUser

# Create your models here.
class Post1(models.Model):
    title = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)

class Friend(models.Model):
    users = models.ManyToManyField(CustomUser)
    active_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='owner1',null=True)


    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get or create(active_user=current_user)
        friends.users.add(new_friend)

    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get or create(active_user=current_user)
        friends.users.remove(new_friend)