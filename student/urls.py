
from django.urls import path,include

from . import views
urlpatterns = [
    path("api/", include("student.api.urls")),
    path('home/', views.home, name='home'),
     path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit_country/<str:pk>/', views.edit_country, name='edit_country'),
    path('studentdelete/', views.deletestudent, name='studentdelete'),
    path('citydelete/', views.deletecity, name='citydelete'),
    path('countrydelete/', views.deletecountry, name='countrydelete'),
    path('studentedit/', views.editstudent, name='studentedit'),
    path('cityedit/', views.editcity, name='cityedit'),
    path('countryedit/', views.editcountry, name='countryedit'),
    path('edit_student/<int:id>/', views.edit_students, name='edit_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('edit-city/<int:id>/', views.edit_city, name='edit_city'),
    path('delete-city/<int:id>/', views.delete_city, name='delete_city'),
    path('delete-country/<str:pk>/', views.delete_country, name='delete_country'),
    path('create-student/', views.create_student, name='create_student'),
    path('create-city/', views.create_city, name='create_city'),
    path('create-country/', views.create_country, name='create_country'),
    path('record1/', views.view_record, name='record1'),
    path('studentdisplay/', views.studentdisplay, name='studentdisplay'),
    path('citydisplay/', views.citydisplay, name='citydisplay'),
    path('countrydisplay/', views.countrydisplay, name='countrydisplay'),
    path('student/', views.student, name='student'),
    path('city/', views.city, name='city'),
    path('country/', views.country, name='country'),
    path('countrycreate/', views.create_country, name='countrycreate'),
    path('citycreate/', views.create_city, name='citycreate'),
    path('studentcreate/', views.create_student, name='studentcreate'),
    
    path('', views.index, name='index'),
    
]
