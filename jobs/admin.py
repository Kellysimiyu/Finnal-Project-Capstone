from django.contrib import admin
from .models import Jobs # and also had to import the jobs model 

# Register your models here.
admin.site.register(Jobs) # registered the Jobs model
