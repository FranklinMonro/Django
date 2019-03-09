from django.db import models

# Create your models here.
class User(models.Model):
    user_first_name = models.CharField(max_length = 128)
    user_last_name = models.CharField(max_length = 128)
    user_email = models.EmailField(max_length = 256, unique = True)

    def __str__(self):
        return self.user_first_name
