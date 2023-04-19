from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,Group,Permission
from rolepermissions.roles import assign_role
from django.db.models.signals import post_save
from django.utils import timezone
import pytz
from django.dispatch import receiver

# Create your models here.

class CustomUserManager(UserManager):
    pass    

class CustomUser(AbstractUser):
    pass

class LecProfile(models.Model):
    LECTURER = 1
    MANAGEMENT = 2
    ROLE_CHOICES = (
    (LECTURER, 'lecturer'),
    (MANAGEMENT, 'management'),
    )
    role= models.PositiveSmallIntegerField(choices=ROLE_CHOICES,null=True,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='lec_profile')
    Employee_no = models.CharField(max_length=100,null=True,blank=True)
    Department = models.CharField(max_length=100,null=True,blank=True)
    Unit = models.CharField(max_length=100,null=True,blank=True) 
    timezone = models.DateTimeField(null=True,blank=True)   
    lec_image = models.FileField(upload_to='profile_image',blank=True)

    
    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LecProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=CustomUser)

class UserProfile(models.Model):
    STUDENT = 1
    STUDENT_REP = 2
    ROLE_CHOICES = (
      (STUDENT, 'student'),
      (STUDENT_REP, 'student_rep'),
    )
    role= models.PositiveSmallIntegerField(choices=ROLE_CHOICES,null=True,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True, related_name='user_profile')
    reg_no = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=True,blank=True)
    course = models.CharField(max_length=100,null=True,blank=True)
    timezone = models.DateTimeField(null=True,blank=True)   
    your_image = models.FileField(upload_to='profile_image1',blank=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=CustomUser)


    