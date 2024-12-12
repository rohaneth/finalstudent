from django import forms
from .models import User,Student,City,Country  # Replace with your actual model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # Or specify specific fields
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        
        
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'