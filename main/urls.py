from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home,name= 'home'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name= 'login'),
    path('logout/',views.logoutview,name='logoutview'), 
    path('register/',views.register,name='register'),
    path('post/',views.postsomething,name='postsomething'),
    path('profile/',views.profile,name='profile'),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
