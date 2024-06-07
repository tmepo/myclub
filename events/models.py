from django.db import models

# Create your models here.
class Venue(models.Model):
    name=models.CharField(max_length=100)
    address=models.DateField
    zip_code=models.CharField(max_length=100)
    web=models.URLField('Website Address')
    email=models.EmailField('Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=100)
    email=models.EmailField('User Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name=models.CharField(max_length=100)
    venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    manager=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    attendes=models.ManyToManyField(MyClubUser,blank=True)


    def __str__(self):
        return self.name
