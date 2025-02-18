from django.db import models
from users.models import User


class Objects(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=1024, null=True)
    class_object = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = "Objects"
    

class DiscrMatr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Objects, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'object'], name='unique_field1_field2')
        ]

    def __str__(self):
        return f"{self.user} - {self.object}"
    

class Roles(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.role}"


class RoleMatr(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    object = models.ForeignKey(Objects, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} - {self.object}"
