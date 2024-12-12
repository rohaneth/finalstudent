
from django.urls import path
from . import views
urlpatterns = [
    path('edit/<int:id>/', views.edit_students, name='edit_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('edit-city/<int:id>/', views.edit_city, name='edit_city'),
    path('delete-city/<int:id>/', views.delete_city, name='delete_city'),
    path('delete-country/<str:pk>/', views.delete_country, name='delete_country'),
    path('create-student/', views.create_student, name='create_student'),
    path('create-city/', views.create_city, name='create_city'),
    path('create-country/', views.create_country, name='create_country'),
    path('record1/', views.view_record, name='record1'),
]
