from django.db import models

# Create your models here.

class Jobs(models.Model):# The first model  with name JObs
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=1000)
    Price = models.IntegerField()
    Location = models.CharField(max_length=20)

    def __str__(self): # Used the f string because it worked perfectly
        return f"{self.Title}"
