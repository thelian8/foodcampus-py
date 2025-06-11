from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, category='student', email=None):
        if not username:
            raise ValueError('Username is required')
        user = self.model(
            username=username,
            phone_number=phone_number,
            category=category,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password, category='admin', email=None):
        user = self.create_user(username, phone_number, password, category, email)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        
    ]
    username = models.CharField(max_length=30, unique=True)  # Username as the unique identifier
    email = models.EmailField(blank=True, null=True)  # Optional email
    phone_number = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # Changed to username
    REQUIRED_FIELDS = ['phone_number', 'category']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin