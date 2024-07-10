from django.urls import path
from app import views

urlpatterns = [
    path('student/', views.studentlist, name='studentlist'),
    path('student/<int:pk>/', views.studentdetails, name='studentdetail'),
    path('combination/', views.combinationlist, name='combinationlist'),
    path('combination/<int:pk>/', views.combinationdetail, name='combination_detail'),
    path('faculty/', views.facultylist, name='faculty_list'),
    path('faculty/<int:pk>/', views.facultydetail, name='facultydetail'),
    path('login/', views.login, name='login'),
    path('student-count/', views.studentcount, name='student-count'),
    path('register/', views.register, name='register'),
    
]
