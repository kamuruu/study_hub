from django.contrib import admin
from .models import Course, Assignment

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'credits', 'created_at')
    search_fields = ('title', 'instructor')
    list_filter = ('credits',)
    inlines = [AssignmentInline]


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'is_completed')
    list_filter = ('is_completed', 'course')
    list_editable = ('is_completed',)
    date_hierarchy = 'due_date'

from .models import Course, Assignment, Student # <-- Import Student

# ... keep your existing CourseAdmin and AssignmentAdmin ...

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')
    search_fields = ('first_name', 'last_name')
    # This creates a great two-column UI for adding/removing courses
    filter_horizontal = ('courses',)