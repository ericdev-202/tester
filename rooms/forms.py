from django.forms import ModelForm,DateTimeInput
from django.contrib.admin import widgets
from django import forms
from rooms import models as rooms_models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = rooms_models.User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = rooms_models.Profile
        fields = ['image']		


class RoomForm(forms.ModelForm):

	class Meta:
		model =  rooms_models.Room
		fields = ['rooms','location','status']

class DocumentForm(forms.ModelForm): 
	class Meta:
		model = rooms_models.Document
		fields = ['description','document']
		
class EmptyroomUpdateForm(forms.ModelForm):
	class Meta:
		model = rooms_models.Emptyroom
		fields = ['rooms']


class EmptyroomForm(forms.ModelForm):

	class Meta:
		model =  rooms_models.Emptyroom
		fields = ['rooms','location','status']	

class StudentForm(forms.ModelForm):

	class Meta:
		model = rooms_models.Student
		fields = ['course','year_of_study','unit','rooms','mtime']

		widgets = {
		'mtime':DateTimeInput(attrs={'type':'mtime'})
		}


class LecturerForm(forms.ModelForm):

	class Meta:
		model = rooms_models.Lecturer
		fields = ['course','unit','rooms','status']		
			
				
class EventsForm(forms.ModelForm):

	class Meta:
		model = rooms_models.Events
		fields = ['title','description']

		# widgets = {
		# 	'time':DateTimeInput(attrs={'type':'time'}),
		# 	'date':DateTimeInput(attrs={'type':'date'})

		# }

class EventForm(forms.ModelForm):
	class Meta:
		model = rooms_models.Event
		fields = ['title', 'description', 'venue', 'mdate', 'mtime']

		widgets = {
		    'mdate':DateTimeInput(attrs={'type':'mdate'}),
			'mtime':DateTimeInput(attrs={'type':'mtime'})
		}


