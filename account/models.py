# from django.db import models
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.


# class User(AbstractUser):
#     is_admin= models.BooleanField('Is admin', default=False)
#     is_student = models.BooleanField('Is student', default=False)
#     is_teacher = models.BooleanField('Is teacher', default=False)
# # Create your models here.


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(Group, related_name='account_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='account_user_permissions')
