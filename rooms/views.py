from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from rooms import models as rooms_models
from django.shortcuts import render,redirect
from rooms import forms as rooms_forms
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rooms.models import CrudUser
from rooms.models import Room, Emptyroom,Events
from django.utils import timezone
from rooms.forms import EventForm 
from django.db.models import Q
from wsgiref.util import FileWrapper
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,Http404	
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from .forms import SignUpForm,CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Profile has been updated successfully')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)




def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'form':form}
	return render(request,'user/register.html',context)


def download(request, path):
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(),content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
		raise Http404	

def files_view(request):
	files = rooms_models.Document.objects.filter(id=request.id)
	return render(request, template_name='user/download.html')

def loginPage(request):
	context = {}
	return render(request,'user/login.html',context)





def activation_sent_view(request):
    return render(request, 'registration/activation_sent.html')


def activate(request,uidb64,token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError,ValueError,OverflowError,user.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user,token):
		user.is_active = True
		user.profile.signup_confirmation = True
		user.save()

		return redirect('home')	
	else:
		return render(request,'activation_invalid.html')



# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     # checking if the user exists, if the token is valid.
#     if user is not None and account_activation_token.check_token(user, token):
#         # if valid set active true 
#         user.is_active = True
#         # set signup_confirmation true
#         user.profile.signup_confirmation = True
#         user.save()
#         login(request,user)
#         return redirect('home')
#     else:
#         return render(request, 'activation_invalid.html')

def signup(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # user.profile.first_name = form.cleaned_data.get('first_name')
            # user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = True
            user.save()
            login = {
               'user':user
            }
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:	
			messages.info(request,'Username OR Password is incorrect')
	context = {}
	return render(request,'registration/login.html',context)		



# def signup(request):
#     if request.method == 'POST':
#         form = rooms_forms.SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = rooms_forms.SignUpForm()
#     return render(request, 'temps/signup.html', {'form': form})


# Create your views here.


# def home(request):
# 	return render(request,'temps/home.html')

# def rooms(request):
# 	form_class = rooms_forms.RoomForm
# 	if request.method == 'POST':
# 		form = form_class(data=request.POST)
# 		if form.is_valid():
# 			Newrooms = Room()
# 			Newrooms.rooms = request.POST.get('rooms')
# 			Newrooms.location = request.POST.get('location')
# 			Newrooms.status = request.POST.get('status')
# 			Newrooms.created = timezone.now()
# 			Newrooms.save()
# 			return redirect('home')
# 		else:
# 			form = form_class
# 	return render(request, 'temps/rooms.html',{'rooms':form_class})
# def rooms(request):
#  	if request.method == 'POST' and request.FILES['myfile']:
#  		myfile = request.FILES['myfile']
#  		fs = FileSystemStorage()
#  		filename = fs.save(myfile.name, myfile)
#  		uploaded_file_url = fs.url(filename)
#  		return render(request, 'temps/rooms.html',{
#  			'uploaded_file_url':uploaded_file_url
#  			})
#  	return render(request,'temps/rooms.html')	


# def signup_view(request):
# 	form = UserCreationForm(request.POST)
# 	if form.is_valid():
# 		form.save()
# 		username = form.cleaned_data.get('username')
# 		password = form.cleaned_data.get('password1')
# 		user = authenticate(username=username,password=password)
# 		login(request,user)
# 		return redirect('home')
# 	return render(request,'signup.html',{'form':form})	

@login_required
def rooms(request): 	
	doc = rooms_models.Document.objects.all()
	if request.method == 'POST':
		form = rooms_forms.DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = rooms_forms.DocumentForm()
	return render(request,'temps/rooms.html',{
		'form':form
		})
	

# def events(request):
# 	form = rooms_forms.EventsForm
# 	events = Events.objects.all()

# 	if request.POST.get('action') == 'post':
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')


# 		obj = Events.objects.create(
# 			title = title,
# 			description = description,
# 			)
# 		user = {'id':obj.id,'title':obj.title,'description':obj.description}
# 		response_data = {
# 		    'user':user
# 		}
# 		return JsonResponse(response_data)
# 	return render(request, 'temps/events.html',{'events':events})	
@login_required
def events(request):
	form_class = rooms_forms.EventForm
	events = Events.objects.all()

	if request.POST.get('action') == 'post':
		title = request.POST.get('title')
		description = request.POST.get('description')

		obj = Events.objects.create(
			title = title,
			description=description,

			)
		user = {'id':obj.id,'title':obj.title,'description':obj.description}

		response_data = {
		   'user':user
		}
		return JsonResponse(response_data)
	return render(request, 'temps/events.html',{'events':events})	

@login_required
def events_update(request):
	id = request.GET.get('id',None)
	title = request.GET.get('title',None)
	description = request.GET.get('description',None)

	obj = Events.objects.get(id=id)
	obj.title = title
	obj.description = description
	obj.save()

	user = {'id':obj.id,'title':obj.title,'description':obj.description}

	response_data = {
	    'user':user
	}
	return JsonResponse(response_data)

@login_required
def events_delete(request):
	id = request.GET.get('id',None)
	Events.objects.get(id=id).delete()
	response_data = {
	    'deleted':True
	}
	return JsonResponse(response_data)


# def events_delete(request):
# 	id = request.GET.get('id',None)
# 	Event.objects.get(id=id).delete()
# 	response_data = {
# 	    'deleted':True
# 	}
# 	return JsonResponse(response_data)


		




	    	 


# def delete(request,id):
# 	obj = Event.objects.get(id=id)
# 	obj.delete()
# 	return JsonResponse(response_data)

# def event(request):
# 	form_class = rooms_forms.EventForm
# 	event = Event.objects.all()
# 	response_data = {}

# 	if request.POST.get('action') == 'post':
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')
# 		venue = request.POST.get('venue')
# 		mdate = request.POST.get('mdate')
# 		mtime = request.POST.get('mtime')

# 		response_data['title'] = title
# 		response_data['description'] = description
# 		response_data['venue'] = venue
# 		response_data['mdate'] = mdate
# 		response_data['mtime'] = mtime


# 		Event.objects.create(
# 			title = title,
# 			description = description,
# 			venue = venue,
# 			mdate = mdate,
# 			mtime = mtime,
# 			)
# 		return JsonResponse(response_data)
      
# 	return render(request, 'temps/event.html',{'event':event})	

@login_required
def student(request):
	form_class = rooms_forms.StudentForm
	student = rooms_models.Student.objects.all()

	if request.POST.get('action') == 'post':
		course = request.POST.get('course')
		unit = request.POST.get('unit')
		year_of_study = request.POST.get('year_of_study')
		rooms = request.POST.get('rooms')
		mtime = request.POST.get('mtime')

		obj = rooms_models.Student.objects.create(
			course = course,
			unit = unit,
			year_of_study = year_of_study,
			rooms = rooms,
			mtime = mtime,
			)
		user = {'course':obj.course,'unit':obj.unit,'year_of_study':obj.year_of_study,'rooms':obj.rooms,'mtime':obj.mtime}
		response_data = {
		    'user':user
		}
		return JsonResponse(response_data)
	return render(request,'temps/students.html',{'student':student})	

# def student(request):	
# 	id = request.GET.get('id',None)
# 	rooms = request.GET.get('rooms',None)

# 	obj = rooms_models.Student.objects.get(id=id)
# 	obj.rooms = rooms
# 	obj.save()

# 	user = {'id':obj.id,'rooms':obj.rooms}
# 	response_data = { 
# 	'user':user
# 	}
# 	return JsonResponse(response_data)


def login(request):
	m = Member.objects.get(username=request.POST['username'])
	if m.password == request.POST['password']:
		request.session['member_id'] = m.id
		return HttpResponse("you're logged in.")
	else:
		return HttpResponse("Your username and password didn't match.")

def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return HttpResponse("you're logged out.")	
@login_required
#creating
def search(request):
	if request.method=='POST':
		srch = request.POST['srh']

		if srch:
			match = rooms_models.Student.objects.filter(Q(course__icontains=srch)|
				                           Q(unit__icontains=srch)
				                           )
			if match:
				return render(request,'temps/search.html',{'sr':match})
			else:
			    messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/search/')
	return render(request,'temps/search.html')

@login_required		     
def event(request):
	# form_class = rooms_forms.EventForm
	event = rooms_models.Event.objects.all()

	if request.POST.get('action') == 'post':
		title1 = request.POST.get('title')
		description1 = request.POST.get('description')
		venue1 = request.POST.get('venue')
		mdate1 = request.POST.get('mdate')
		mtime1 = request.POST.get('mtime')


		obj = rooms_models.Event.objects.create(
			title = title1,
			description =description1,
			venue = venue1,
			mdate = mdate1,
			mtime = mtime1,
			)
		user = {'id':obj.id,'title':obj.title,'description':obj.description,'venue':obj.venue,'mdate':obj.mdate,'mtime':obj.mtime}

		response_data = {
		   'user':user
		}
		return JsonResponse(response_data)
	return render(request, 'temps/event.html',{'event':event})	
#updating
@login_required
def event_update(request):
	id1 = request.GET.get('id',None)
	title1 = request.GET.get('title',None)
	description1 = request.GET.get('description',None)
	venue1 = request.GET.get('venue',None)
	mdate1 = request.GET.get('mdate',None)
	mtime1 = request.GET.get('mtime',None)

	obj = rooms_models.Event.objects.get(id= id1)
	obj.title = title1
	obj.description = description1
	obj.venue = venue1
	obj.mdate = mdate1
	obj.mtime = mtime1
	obj.save()

	user = {'id':obj.id,'title':obj.title,'description':obj.description,'venue':obj.venue,'mdate':obj.mdate,'mtime':obj.mtime}
	response_data = {
        'user':user
	}
	return JsonResponse(response_data)

@login_required
def emptyrooms(request):
	form_class = rooms_forms.EmptyroomForm
	emptyrooms = Emptyroom.objects.all()

	if request.POST.get('action') == 'post':
		rooms = request.GET.get('rooms')
		location = request.POST.get('location')

		obj = Emptyroom.objects.create(
			rooms = rooms,
			location = location,
			)
		user = {'id':obj.id,'rooms':obj.rooms,'location':obj.location}

		response_data = {
		   'user':user
		}
		return JsonResponse(response_data)
	return render(request, 'temps/emptyrooms.html',{'emptyrooms':emptyrooms})		

@login_required
def emptyrooms_up(request):	
	id1 = request.GET.get('id',None)
	rooms = request.GET.get('rooms',None)

	obj = Emptyroom.objects.get(id=id)
	obj.rooms = rooms
	obj.save()

	user = {'id':obj.id,'rooms':obj.rooms}
	response_data = {
	   'user':user
	}
	return JsonResponse(response_data)
	    

	    
	
#deleting

@login_required
def event_delete(request):
	id = request.GET.get('id',None)
	rooms_models.Event.objects.get(id=id).delete()
	response_data = {
	    'deleted':True
	}
	return JsonResponse(response_data)


# def students(request):
# 	form_class = rooms_forms.StudentForm
# 	student = rooms_models.Student.objects.all()
# 	if request.POST.get('action') == 'post':
# 		course = request.POST.get('course')
# 		year_of_study = request.POST.get('year_of_study')
# 	    unit = request.POST.get('unit')
#         rooms  = request.POST.get('rooms')

# 	    obj = rooms_models.Student.objects.create(
# 	       	course = course,
# 	       	year_of_study = year_of_study,
# 	       	unit = unit,
# 	       	rooms = rooms,
#         	)
#         user = {'course':obj.course,'year_of_study':obj.year_of_study,'unit':obj.unit,'rooms':obj.rooms}

#         data = {
#         'user':user
#         }
#         return JsonResponse(data)
#     # return render(request,'temps/',{'student':student})    










# def events(request):
# 	form_class = rooms_forms.EventsForm
# 	if request.method == 'POST':
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')
# 		date = request.POST.get('date')
# 		time = request.POST.get('time')
# 		venue = request.POST.get('venue')
# 		created = timezone.now()
# 		feedback = rooms_models.Events.objects.create(
# 				venue=venue,
# 			    title=title,
# 				description=description,
# 				date=date,
# 				time=time,
# 				)
# 		feedback.save()
# 		data = {
# 				venue:venue,
# 				title:title,
# 				description:description,
# 				date:date,
# 				time:time,
# 				created:created
# 			}
	    

# 		return JsonResponse({'data':'data'})
# 	return JsonResponse({'data':'Error'})

# 		# 	NewEvents.save()
# 		# 	return redirect('home')
# 		# else:
# 		#     form =form_class	

# 	return render(request, 'temps/events.html',{'rooms':form_class})		



# def emptyrooms(request):
# 	form_class = rooms_forms.EmptyroomForm
# 	if request.method == 'POST':
# 		form = form_class(data=request.POST)
# 		if form.is_valid():
# 			Newrooms = Room()
# 			Newrooms.rooms = request.POST.get('rooms')
# 			Newrooms.location = request.POST.get('location')
# 			Newrooms.status = request.POST.get('status')
# 			Newrooms.created = timezone.now()
# 			Newrooms.save()
# 			return redirect('home')
# 		else:
# 			form = form_class
# 	return render(request,'temps/emptyrooms.html',{'rooms':form_class})

# def students(request):
# 	form_class = rooms_forms.StudentForm
# 	if request.method == 'POST':
# 		form = form_class(data=request.POST)
# 		if form.is_valid():
# 			Newrooms = rooms_models.Student()
# 			Newrooms.course= request.POST.get('course')
# 			Newrooms.rooms = request.POST.get('rooms')
# 			Newrooms.year_of_study = request.POST.get('year_of_study')
# 			Newrooms.unit = request.POST.get('unit')
# 			Newrooms.created = timezone.now()
# 			Newrooms.save()
# 			return redirect('home')
# 		else:
# 			form = form_class
# 	return render(request, 'temps/students.html',{'rooms':form_class})

@login_required
def lecturers(request):
	form_class = rooms_forms.LecturerForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			Newrooms =rooms_models.Lecturer()
			Newrooms.rooms = request.POST.get('rooms')
			Newrooms.course= request.POST.get('course')
			Newrooms.unit= request.POST.get('unit')
			Newrooms.status = request.POST.get('status')
			Newrooms.created = timezone.now()
			Newrooms.save()
			return redirect('home')
		else:
			form = form_class
	return render(request, 'temps/lecturers.html',{'rooms':form_class})		



# def emptyrooms(request):
# 	form_class = rooms_forms.EmptyroomForm
# 	emptyrooms = Emptyroom.objects.all()
# 	response_data = {}

# 	if request.POST.get('action') == 'post':
# 		rooms = request.GET.get('rooms')
# 		location = request.POST.get('location')

# 		response_data['rooms'] = rooms
# 		response_data['location'] = location


# 		Emptyroom.objects.create(
# 			rooms = rooms,
# 			location = location,
# 			)
# 		return JsonResponse(response_data)
# 	return render(request, 'temps/emptyrooms.html',{'emptyrooms':emptyrooms})	



# class CrudView(ListView):
#     model = CrudUser
#     template_name = 'temps/home.html'
#     context_object_name = 'users'

# def crudview(request):
# 	model = CrudUser
# 	template_name = 'temps/home.html'
# 	context_object_name = 'users'

def home(request):
	model = CrudUser
	cruduser = CrudUser.objects.all()
	context_object_name = 'users'
	if request.POST.get('action') == 'post':
		name1 = request.POST.get('name',None)
		address1 = request.POST.get('address', None)
		age1 = request.POST.get('age', None)

		obj = CrudUser.objects.create(
			name = name1,
			address = address1,
			age = age1,
			)
		user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

		data = {
		'user': user
		}
		return JsonResponse(data)
	return render(request, 'temps/home.html', {'cruduser':cruduser})	


def Update(request):
	model = CrudUser
	cruduser = CrudUser.objects.all()
	context_object_name = 'users'
	if request.GET.get('action') == 'post':
		id1 = request.GET.get('id',None)
		name1 = request.GET.get('name',None)
		address1 = request.GET.get('address',None)
		age1 = request.GET.get('age',None)

		obj = CrudUser.objects.get(id=id1)
		obj.name = name1
		obj.address = address1
		obj.age = age1
		obj.save()

		user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

		data = {
		    'user': user
		}

		return JsonResponse(data)



# class CreateCrudUser(ListView):
#     def  get(self, request):
#         name1 = request.GET.get('name', None)
#         address1 = request.GET.get('address', None)
#         age1 = request.GET.get('age', None)

#         obj = CrudUser.objects.create(
#             name = name1,
#             address = address1,
#             age = age1
#         )

#         user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

#         data = {
#             'user': user
#         }
#         return JsonResponse(data)	

# class UpdateCrudUser(ListView):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         name1 = request.GET.get('name', None)
#         address1 = request.GET.get('address', None)
#         age1 = request.GET.get('age', None)

#         obj = CrudUser.objects.get(id=id1)
#         obj.name = name1
#         obj.address = address1
#         obj.age = age1
#         obj.save()

#         user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

#         data = {
#             'user': user
#         }
#         return JsonResponse(data)        


    
# class DeleteCrudUser(ListView):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         CrudUser.objects.get(id=id1).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)