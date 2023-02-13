from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings  # for model being used


# Create your models here.
class CustomUser(AbstractUser):
    GROUPS = (
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=100, choices=GROUPS, default='regular')
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField('Description', max_length=600, default='', blank=True)

    def __str__(self):
        return self.email


# Stores the swimmer details with link to guardians
# class Swimling(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     first_name = models.CharField(max_length=255, blank=True,
#                                   null=True, )
#     last_name = models.CharField(max_length=255, blank=True,
#                                  null=True, )
#     dob = models.DateField(null=True)
#     school_role_number = models.CharField(max_length=6, blank=True,
#                                           null=True, )
#     description = models.TextField('Notes', max_length=600, default='', blank=True)
#     # id from student details table in wordpress site
#     wp_student_id = models.IntegerField(null=True)
#
#     def __str__(self):
#         return self.first_name + "  " + str(self.last_name)
