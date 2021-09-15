from django.urls import path
from . import views

urlpatterns=[
    path('alldep/',views.allDepartmentsView,name='all-departments'),
    path('createdep/',views.addDepartmentView,name='add-dep'),
    path('updatedep/<int:id>',views.updateDepartmentView,name='update-dep'),
    path('deletedep/<int:id>',views.deleteDepartmentView,name='delete-dep'),
    path('addteacher/',views.addTeacherView,name='add-teacher'),
    path('allteachers/',views.allTeachersView,name='all-teachers'),
    path('updateTeacher/<int:id>',views.updateTeacherView,name='update-teacher'),
    path('deleteTeacher/<int:id>',views.deleteTeacherView,name='delete-teacher'),
    path('addstud/',views.addStudentView,name='add-student'),
    path('allstuds/',views.allStudentsView,name='all-students'),
    path('updateStud/<int:id>',views.updateStudentView,name='update-student'),
    path('deleteStud/<int:id>',views.deleteStudentView,name='delete-student'),
    path('search/',views.searchView,name='search')
]