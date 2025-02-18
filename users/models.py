from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if username is None:
            raise TypeError("Users must have a email")

        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(
        max_length=25,
        editable=False,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\d!@#$%^&*()_+]+$",
                message=("Invalid password"),
                code="invalid_password",
            ),
        ],
    )
    access_class = models.IntegerField(default=0, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username