from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)

GENDER_CHOICES = (
    ("Male", "Male"), 
    ("Female", "Female"),
)

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=150)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=15)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"))
    address = models.TextField(verbose_name=_("Address"))
    gender = models.CharField(verbose_name=_("Gender"), max_length=10, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(verbose_name=_("Profile Picture"), upload_to='profile_pics/', null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
