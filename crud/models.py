from django.db import models
# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=False, unique=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False,unique=True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    contacts = models.ManyToManyField(Contact, blank=True, related_name='groups' )

    def __str__(self):
        return self.name

    
    
   

    
