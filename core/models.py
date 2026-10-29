from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=150)
    instructor = models.CharField(max_length=100, blank=True)
    credits = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    # Links this assignment to a specific course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.course.title})"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    enrollment_date = models.DateField(auto_now_add=True)
    
    # This creates the Many-to-Many relationship.
    # blank=True allows a student to be created without any courses initially.
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"