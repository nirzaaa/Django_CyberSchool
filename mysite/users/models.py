from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # is user is deleted -> profile is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class BadProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # is user is deleted -> profile is deleted
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image = models.FileField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # is user is deleted -> profile is deleted
    file = models.FileField(default='default.jpg', upload_to='resume_files')

    def __str__(self):
        return f'{self.user.username} Resume'
