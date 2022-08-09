from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    email_id = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name
