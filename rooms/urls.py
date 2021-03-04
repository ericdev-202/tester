from django.urls import path
from rooms import views as r_views
from rooms import views 
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rooms import models as r_models



urlpatterns = [
    # path('',r_views.home,name='home'),   
    path('event/',r_views.event,name='event'),
    path('register/',r_views.registerPage,name='register'),
    path('new/',r_views.loginPage,name='log'),
    path('profile',r_views.profile,name='profile'),
    path('download/',r_views.download,{'document_root':settings.MEDIA_ROOT}),
    # path('accounts/ password_change/done/', name='password_change_done'),
    # path('accounts/ password_reset/', name='password_reset'),
    # path('accounts/ password_reset/done/', name='password_reset_done'),
    # path('accounts/ reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # pathe('accounts/ reset/done/', name='password_reset_complete'),

    # path('signup/', r_views.signup_view, name="signup"),
    path('update',r_views.event_update,name='event_update'),
    # path(r'^event/(?P<pk>\d+)/update/', r_views.event_update, name='event_update'),
    path('delete',r_views.event_delete,name='event_delete'),
    path('delete',r_views.events_delete,name='events_delete'),
    path('events/',r_views.events,name='events'),
    path('rooms/',r_views.rooms,name='rooms'),
    path('emptyrms/',r_views.emptyrooms,name='emptyrooms'),
    path('emptyrms/',r_views.emptyrooms_up,name='emptyrooms_up'),
    path('student/',r_views.student,name='student'),
    path('search/',r_views.search,name='search'),
    path('lecturers/',r_views.lecturers,name='lecturers'),
    # path(r'^events/',r_views.Events,name='events'),
    path('events/update/',r_views.events_update,name='events_update'),

    # path('',  views.CrudView.as_view(), name='home'),
    # path('home/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    # path('home/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    # path('home/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('',r_views.home,name='home'),
    # path('cr',r_views.Create,name='create'),
    path('up',r_views.Update,name='update'),
    # path('sign',r_views.sign,name='sign'),


]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
