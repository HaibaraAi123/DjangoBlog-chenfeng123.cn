from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phonenum = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


# 信号接收函数 新建user时调用
@receiver(post_save, sender=User)
def creat_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 更新时自动调用
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()