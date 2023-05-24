from django.urls import path
from django.contrib import admin
from django.urls.conf import include  
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('', views.home, name = 'home'),
    path('notification/', views.notify, name = 'notify'),
    path('guide/', views.guide, name = 'guide'),

    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name = 'register'),
    path('auth/', views.admin, name = 'admin'),
    path('authdoubts/', views.admindoubts, name = 'admindoubts'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)