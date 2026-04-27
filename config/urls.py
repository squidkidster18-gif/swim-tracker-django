from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('students/', views.students, name='students'),
    path('add-student/', views.add_student, name='add_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('levels/', views.levels, name='levels'),
]