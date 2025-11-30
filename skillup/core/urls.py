from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register_view, name='register'),
   path('add-skill/', views.add_skill, name='add_skill'),
   path('edit-skill/<int:id>/', views.edit_skill, name='edit_skill'),
   path('delete-skill/<int:id>/', views.delete_skill, name='delete_skill'),
   # ⚡ Fix here: point to the correct function name
   path('career-suggestions/', views.career_suggestions, name='career_suggestions'),
   path('upload-resume/', views.upload_resume, name='upload_resume'),
   path('admin-analytics/', views.admin_analytics, name='admin_analytics'),
]
