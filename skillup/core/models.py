from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)  # Add this line to prevent NOT NULL errors

    def __str__(self):
        return f"{self.skill_name} - {self.user.username}"


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, blank=True)
   email = models.EmailField(blank=True)
   age = models.IntegerField(null=True, blank=True)
   resume = models.FileField(upload_to='resumes/', blank=True, null=True)


   def __str__(self):
       return self.user.username
