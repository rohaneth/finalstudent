from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from student.models import Student,City,Country
from django.shortcuts import render



from .serializers import StudentSerializer,CitySerializer,CountrySerializer




@api_view(['GET'])
def getRoutes(request):
    return render(request, 'api.html')

@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCitys(request):
    citys = City.objects.all()
    serializer = CitySerializer(citys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCountries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)
