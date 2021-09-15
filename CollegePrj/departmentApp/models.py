from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=30)
    dep_year_of_establishment=models.IntegerField()
    dep_course_duration=models.IntegerField()

    def __str__(self):
        return f'{self.dep_name}'

class Teacher(models.Model):
    department=models.ManyToManyField(Department)
    t_name=models.CharField(max_length=30)
    t_salary=models.FloatField()
    t_date_of_joining=models.DateField()

    def __str__(self):
        return f'{self.t_name},{self.t_salary},{self.t_date_of_joining},{self.department}'

class Student(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    roll_no=models.IntegerField()
    s_name=models.CharField(max_length=30)
    s_email = models.EmailField()

    def __str__(self):
        return f'{self.roll_no},{self.s_name}'
        
