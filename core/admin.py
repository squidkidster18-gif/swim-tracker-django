from django.contrib import admin
from .models import StudentLevel, Student, LessonNote

admin.site.register(StudentLevel)
admin.site.register(Student)
admin.site.register(LessonNote)
