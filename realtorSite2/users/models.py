from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
from datetime import datetime




class UsersManger(BaseUserManager):
    def create_user(self, email, user_name ,password,mobile_phone,**other_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email)

        user = self.model(
            email=email,
            user_name=user_name,
            mobile_phone=mobile_phone,
            **other_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, user_name ,password,mobile_phone,**other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError("super user must be assigned is_staff = True")
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError("super user must be assigned is_superuser = True")
        
       
      
        return self.create_user(email,user_name,password,mobile_phone,**other_fields)
        
        

def user_profile_pic_path(instance, filename):
        return f'accounts/profile_pics/user_{instance.id}/{filename}'
    
    
class NewUser(AbstractBaseUser,PermissionsMixin):
    

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_name=models.CharField(max_length=150,unique=True)
    first_name=models.CharField(max_length=150,null=True,blank=True)
    last_name=models.CharField(max_length=150,null=True,blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    mobile_phone = models.IntegerField(default='0109999999')

    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    

    profile_pic=models.ImageField( upload_to=user_profile_pic_path, max_length=200,null=True,blank=True)

    REQUIRED_FIELDS = ['user_name','mobile_phone'] 
    USERNAME_FIELD = 'email'

    objects=UsersManger()
    
    def __str__(self):
        return f'{self.user_name}'
    
    @classmethod
    def get_all_users(cls):
        return cls.objects.all()