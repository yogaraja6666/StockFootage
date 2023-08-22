
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='uploadimage'),
    path('posts/', views.profile, name='profile'),
    path('search/', views.home, name='search'),
    path('suggest_keywords/', views.suggest_keywords, name='suggest_keywords'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('download/<int:photo_id>/', views.download, name='download'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)