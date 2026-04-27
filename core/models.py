from django.db import models

class StudentLevel(models.Model):
    level_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.level_name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    parent_name = models.CharField(max_length=100, blank=True)
    parent_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    current_level = models.ForeignKey(StudentLevel, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LessonNote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lesson_notes')
    lesson_date = models.DateField()
    previous_notes = models.TextField(blank=True)
    next_goal = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.lesson_date}"