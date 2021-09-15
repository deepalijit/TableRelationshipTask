from django import forms
from .models import Department,Teacher,Student

class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        labels = {
            "dep_name": "Department Name",
            "dep_year_of_establishment": "Department's Year of establishment",
            "dep_course_duration": "Course Duration"

        }
        fields='__all__'

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields='__all__'

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
