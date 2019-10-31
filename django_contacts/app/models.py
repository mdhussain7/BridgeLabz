from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    info = models.CharField(max_length=50, choices=(
        ('brother','Brother'),
        ('sister','Sister'),
        ('friend','Friend'),
        ('enemy','Enemy')
    ))
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
