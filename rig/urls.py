
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import EventUpdateView

urlpatterns = [
    
    path('',views.index, name='index'),
    path('user_login/',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='user_login'),
    #path('user_login/',views.login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('individual/',views.individual, name='individual'),    
    path('company/', views.company, name='company'), 
    path('download_detail/<int:pk>', views.download_detail, name='download_detail'),
    path('download_doc/<int:pk>', views.download_doc, name='download_doc'),
    path('download_img/<int:pk>', views.download_img, name='download_img'),
   
   
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
