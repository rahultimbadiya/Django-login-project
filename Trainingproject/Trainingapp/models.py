from django.db import models

class UserData(models.Model):
    Firstname = models.CharField(max_length=25)
    Lastname = models.CharField(max_length=25)
    Username = models.CharField(max_length=25)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username