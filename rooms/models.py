from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.contrib import messages



            


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    # def __str__(self):
    # 	return '{self.user.username} profile'

    # def save(self):	
    # 	super().save()

    # 	img = Image.open(self.image.path)

    # 	if img.height >300 or img.width >300:
    # 		output_size = (300,300)
    # 		img.thumbnail(output_size)
    # 		img.save(self.image.path)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # instance.profile.save()



status=(
		('Open','Open'),
		('Closed','Closed'),
		('Occupied','Occupied'),
		('Empty','Empty')
		)
courses=(
        ('BIT','BIT'),
        ('BBIT','BBIT'),
        ('BCS','BCS'),
        ('BCSF','BCSF'),
        ('BMC', 'BMC')
	    )

class Room(models.Model):
	rooms = models.CharField(max_length=254)
	location = models.CharField(max_length=150)
	status =models.CharField(max_length=200, choices=status)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.rooms

	class Meta:
		verbose_name_plural = 'Room'
		ordering = ['-created']

class Document(models.Model):		
	description = models.CharField(max_length=255,blank=True)
	document = models.FileField(upload_to='document/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

class Emptyroom(models.Model):
	rooms = models.CharField(max_length=254)
	location = models.CharField(max_length=150)
	status = models.CharField(max_length=200, choices=status)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.rooms

	class Meta:
		verbose_name_plural = 'Emptyroom'
		ordering = ['-created']


class Student(models.Model):
	course = models.CharField(max_length=254, choices=courses)
	year_of_study = models.CharField(max_length=200)
	unit = models.CharField(max_length=254)
	rooms =models.CharField(max_length=254)
	mtime = models.TimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
			
			
	def __str__(self):
		return self.rooms

	class Meta:
		verbose_name_plural = 'Student'
		ordering = ['-created']

class Lecturer(models.Model):
	course = models.CharField(max_length=254, choices=courses)
	unit = models.CharField(max_length=254)
	rooms =models.CharField(max_length=254)
	status = models.CharField(max_length=200, choices=status)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

            	
			
	def __str__(self):
		return self.rooms

	class Meta:
		verbose_name_plural = 'Lecturer'
		ordering = ['-created']


						

class Events(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.title

	# def __str__(self):
	# 	return self.title

	# class Meta:
	# 	verbose_name_plural = 'Events'
	# 	ordering = ['-created']
					
						
	# 		

class Event(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	venue = models.CharField(max_length=150)
	mdate = models.DateField()
	mtime = models.TimeField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

