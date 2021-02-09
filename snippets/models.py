from django.db import models

# Create your models here.
class Name(models.Model):
    created=models.DateTimeField(auto_now_add= True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
