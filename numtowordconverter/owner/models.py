from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class owner(models.Model):
    Result=models.CharField(max_length=120,unique=True)

    Number=models.PositiveIntegerField(default=0)
    # copies=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.owner