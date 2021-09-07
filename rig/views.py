from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings as conf_settings
from django.core.files.storage import FileSystemStorage
from .forms import EventForm
from .models import Event
from .filters import EventFilter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import  UserPassesTestMixin
import os
from django.http import FileResponse
import mimetypes
from .models import Categories
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile
from django.contrib.auth.models import User








from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

NUM_ROWS = conf_settings.PAGINATION_ROWS
# Create your views here.

def index(request):
    category_list=Categories.objects.all()
    return render(request, 'rig/index.html', {'title': 'Index','categories':category_list})
    
def home(request):

    return render(request, 'rig/edit_list.html', {'title': 'Home'})

def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            users_without_profile = User.objects.filter(profile__isnull=True)
            for user in users_without_profile:
                Profile.objects.create(user=user)
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def company(request):
    return render(request, 'rig/company.html', {'title': 'Company'})

def individual(request):
    return render(request, 'rig/individual.html', {'title': 'Individual'})

def profile(request):
    return render(request, 'rig/individual.html', {'title': 'Profile'})


def eventlist(request):
   
    context={}
    post_list=Event.objects.all()
    
    filtered_posts = EventFilter(request.GET, queryset=post_list)
    context['filter'] = filtered_posts

    #page=1 by default
    urlmeta=request.META['QUERY_STRING']
    if urlmeta=='':
        urlmeta='?page=1'

    # CURRENT_URL=urlmeta


#    urlmeta=request.META['QUERY_STRING']
    if urlmeta=='':
        urlmeta='?name=&location=&prayed=&rig_choices=&rig_date='

    CURRENT_URL=urlmeta

    filtered_posts.qs.update(current_url=urlmeta)

    #used for pagination



    paginated_rs = Paginator(filtered_posts.qs, NUM_ROWS)
    page_number = int(request.GET.get('page', '1'))
    page_obj = paginated_rs.get_page(page_number)
    context['page_obj']= page_obj
    
    

    request.session['CURRENT_URL']=CURRENT_URL

    return render(
        request, 
        'rig/edit_list.html', 
        {'context': context},
    )

class EventUpdateView(UserPassesTestMixin, UpdateView):
    model = Event
    
    def get_success_url(self):
        root_url = reverse_lazy('home') 

        # if self.object.current_url == None:
        #     self.object.current_url=''
            

        # myurl=root_url+"?"+self.object.current_url
        messages.success(self.request, "Record has been updated")
        return root_url
    

    
    fields = ['name','location','rig_choices','description','rig_image','document']

    def __init__(self, *args, **kwargs):                    
        super(EventUpdateView, self).__init__(*args, **kwargs)   
        instance = getattr(self, 'instance', None)
            
    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        quiz = self.get_object()
        return True   

  

def eventupdate(request, pk=None): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    if pk:
        obj = get_object_or_404(Event, id = pk) 
  
    # pass the object as instance in form 
    form = EventForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/home") 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "rig/edit.html", context) 


def eventdelete(request, pk=None): 
    # dictionary for initial data with  
    # field names as keys 
     instance = Event.objects.get(id=pk)
     instance.delete()
     return HttpResponseRedirect("/home") 
  


      
    

def eventdetail(request, pk=None):
    context ={} 
    context["data"] = Event.objects.get(id = pk)
    return render(request, "rig/detail.html", context) 

def download_detail(request, pk=None):
    context ={} 
    context["data"] = Event.objects.get(id = pk)
    return render(request, "rig/download_detail.html", context) 





def download_doc(request, pk=None):
    obj = Event.objects.get(id = pk)
    file_path = obj.document.path
    #file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            response = HttpResponse(fh, content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_img(request, pk=None):
    obj = Event.objects.get(id = pk)
    file_path = obj.rig_image.path
    #file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            response = HttpResponse(fh, content_type=mime_type)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404