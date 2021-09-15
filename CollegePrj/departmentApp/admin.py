from django.contrib import admin
from .models import Department,Teacher,Student

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dep_name','dep_year_of_establishment','dep_course_duration']

admin.site.register(Department,DepartmentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['t_name','t_salary','t_date_of_joining']

admin.site.register(Teacher,TeacherAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=['roll_no','s_name','s_email','department']

admin.site.register(Student,StudentAdmin)
