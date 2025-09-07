
from django.contrib import admin
from django.urls import path
from nt1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/ ', auth_views.LoginView.as_view(template_name='ht_files/login.html'),name='login'),
    path('logout/ ', auth_views.LogoutView.as_view(template_name='ht_files/logout.html'),name='logout'),
    path('register/' ,views.register, name='register'),
    path('n_d/<int:id>/',views.note_detail, name='note_detail'),
    path('delete/', views.delete, name='delete')

]
