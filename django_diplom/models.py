from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class Company(models.Model):
    name = models.CharField(max_length=128)
    balance = models.IntegerField(null=True, blank=True)
    next_meet = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


class Worker(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    specialist = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


class SellCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super users must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super users must have is_superuser=True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Super users must have is_active=True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_django_hw',
        related_query_name='user_django_hw',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_django_hw',
        related_query_name='user_django_hw',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"User({self.id}), with email {self.email}"

