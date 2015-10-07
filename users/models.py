from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserDetails(models.Model):
    user = models.OneToOneField(User, unique=True)
    phone = models.IntegerField(null=True,blank=True)

'''
class Address(models.Model):
    address = models.CharField(max_length=255, blank=True)
    locality = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=15, blank=True)


class UserProfile(models.Model):
    GENDERS = (('male', 'Male'),('female', 'Female'))
    user = models.OneToOneField(User, unique=True)
    gender = models.CharField(max_length=20, null=True, blank=True,
                                  choices=GENDERS)
    phone = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    #address = models.ForeignKey(Address , null=True)
    address = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return u'%s profile' % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
'''