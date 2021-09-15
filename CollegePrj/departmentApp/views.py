from django.shortcuts import render,redirect
from .models import Department,Teacher,Student
from .forms import DepartmentModelForm,TeacherModelForm,StudentModelForm
from django.http import HttpResponse


# Create your views here.
def addDepartmentView(request):
    form = DepartmentModelForm()
    if request.method=='POST':
        print('post request')
        form=DepartmentModelForm(request.POST)
        if form.is_valid:
            form.save()
            print('department created')
            return redirect('all-departments')
    template_name='departmentApp/createDepartment.html'
    context={'form':form}
    return render(request,template_name,context)

def allDepartmentsView(request):
    deps = Department.objects.all()
    template_name='departmentApp/allDepartments.html'
    context={'deps':deps}
    return render(request,template_name,context)

def updateDepartmentView(request,id):
    dep=Department.objects.get(id=id)
    form = DepartmentModelForm(instance=dep)
    if request.method=='POST':
        form=DepartmentModelForm(request.POST,instance=dep)
        form.save()
        return redirect('all-departments')
    template_name = 'departmentApp/createDepartment.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteDepartmentView(request,id):
    obj = Department.objects.get(id=id)
    data = Teacher.objects.filter(department=obj)
    print(data)
    for i in data:
        print(i)
        for j in i.department.all():
            print(j)
            if len(i.department.all())==1 and j==obj:
                i.delete()
    obj.delete()
    return redirect('all-departments')

def addTeacherView(request):
    form = TeacherModelForm()
    if request.method=='POST':
        print('post request')
        form=TeacherModelForm(request.POST)
        if form.is_valid:
            form.save()
            print('Teacher added')
            return redirect('all-teachers')
            #return HttpResponse('teacher added')
    template_name='departmentApp/addTeacher.html'
    context={'form':form}
    return render(request,template_name,context)

def allTeachersView(request):
    teachers = Teacher.objects.all()
    template_name='departmentApp/allTeachers.html'
    context={'teachers':teachers}
    return render(request,template_name,context)

def updateTeacherView(request,id):
    teacher=Teacher.objects.get(id=id)
    form = TeacherModelForm(instance=teacher)
    if request.method=='POST':
        form=TeacherModelForm(request.POST,instance=teacher)
        form.save()
        return redirect('all-teachers')
    template_name = 'departmentApp/updateTeacher.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteTeacherView(request,id):
    obj = Teacher.objects.get(id=id)
    obj.delete()
    return redirect('all-teachers')

def addStudentView(request):
    form = StudentModelForm()
    if request.method=='POST':
        print('post request')
        form=StudentModelForm(request.POST)
        if form.is_valid:
            form.save()
            print('Student added')
            return redirect('all-students')
            #return HttpResponse('Student added')
    template_name='departmentApp/addStudent.html'
    context={'form':form}
    return render(request,template_name,context)

def allStudentsView(request):
    students = Student.objects.all()
    template_name='departmentApp/allStudents.html'
    context={'students':students}
    return render(request,template_name,context)

def updateStudentView(request,id):
    student=Student.objects.get(id=id)
    form = StudentModelForm(instance=student)
    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=student)
        form.save()
        return redirect('all-students')
    template_name = 'departmentApp/updateStudent.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteStudentView(request,id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('all-students')

def searchView(request):
    query = request.GET['query']
    '''
    obj = Department.objects.get(dep_name=query)
    print(f'obj={obj}')
    teachers=Teacher.objects.filter(department=obj)
    print(teachers)
    context={'teachers':teachers}
    template_name='departmentApp/search.html'
    return render(request,template_name,context)
    '''
    print(query)
    stu = Student.objects.filter(s_name__icontains=query)
    print(stu)
    teacher = Teacher.objects.filter(t_name__icontains=query)
    print(teacher)
    context={'stu':stu,'teacher':teacher}
    template_name = 'departmentApp/search.html'
    return render(request,template_name,context)


