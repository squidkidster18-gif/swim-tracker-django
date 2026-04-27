from django.shortcuts import render, redirect
from .models import Student, StudentLevel

def home(request):
    students = Student.objects.all()
    return render(request, 'core/home.html', {'students': students})

def students(request):
    students = Student.objects.all()
    return render(request, 'core/students.html', {'students': students})  

from django.shortcuts import render, redirect

def add_student(request):
    levels = StudentLevel.objects.all()

    if request.method == 'POST':
        level_id = request.POST.get('current_level')

        Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            current_level_id=level_id if level_id else None
        )
        return redirect('students')

    return render(request, 'core/add_student.html', {'levels': levels})

from django.shortcuts import redirect

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students')

def levels(request):
    levels = StudentLevel.objects.all()
    return render(request, 'core/levels.html', {'levels': levels})