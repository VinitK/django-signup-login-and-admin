from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete='CASCADE')

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username

    # first_name = models.CharField(max_length=128)
    # last_name = models.CharField(max_length=128)
    # email = models.EmailField(max_length=256, unique=True)

class School(models.Model):

    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mainApp:detail", kwargs={'pk':self.pk})


class Student(models.Model):

    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete='CASCADE')

    def __str__(self):
        return self.name
