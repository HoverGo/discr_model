from django.db import models
from users.models import User


class ObjectsDiscr(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=1024, null=True)
    class_object = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ObjectDiscr'
        verbose_name_plural = "ObjectsDiscr"
    

class DiscrMatr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discr_object = models.ForeignKey(ObjectsDiscr, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'discr_object'], name='unique_field1_field2')
        ]

    def __str__(self):
        return f"{self.user} - {self.discr_object}"