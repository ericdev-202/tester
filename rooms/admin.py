from django.contrib import admin


# Register your models here.
from rooms import models as rooms_models
from .models import Profile


class CrusUserAdmin(admin.ModelAdmin):
    list_display = ['name','address','age']

class DocumentAdmin(admin.ModelAdmin):    
	list_display = ['description','document','uploaded_at']

class RoomAdmin(admin.ModelAdmin):
	list_display = ['rooms','location','status','created','modified']

class EmptyroomAdmin(admin.ModelAdmin):
	list_display = ['rooms','location','status','created','modified']

class StudentAdmin(admin.ModelAdmin):
	list_display =['course','year_of_study','unit','rooms','mtime','created','modified']

class LecturerAdmin(admin.ModelAdmin):
	list_display =['course','unit','rooms','status','created','modified']	
				

class EventsAdmin(admin.ModelAdmin):
	list_display = ['title','description']

class EventAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'venue', 'mdate', 'mtime']

class ProfileAdmin(admin.ModelAdmin):
 	list_display = ['image']




admin.site.register(rooms_models.Profile,ProfileAdmin)
admin.site.register(rooms_models.CrudUser,CrusUserAdmin)
admin.site.register(rooms_models.Document,DocumentAdmin)
admin.site.register(rooms_models.Room,RoomAdmin)
admin.site.register(rooms_models.Emptyroom,EmptyroomAdmin)	
admin.site.register(rooms_models.Student,StudentAdmin)
admin.site.register(rooms_models.Lecturer,LecturerAdmin)
admin.site.register(rooms_models.Events,EventsAdmin)
admin.site.register(rooms_models.Event,EventAdmin)