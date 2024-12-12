from django.shortcuts import render, get_object_or_404, redirect
from student.models import Country, City, Student, Company,User
from .forms import StudentForm,CityForm,CountryForm  # Replace with your form

def delete_country(request, pk):
    students = Student.objects.all()
    city_record = City.objects.all()
    countrys = Country.objects.all()
    #delete conuntry where countryneme is pk
    countrys = Country.objects.get(country_name=pk)
    countrys.delete()
    
    return render(request, 'record.html', {'stud12': students, 'city12': city_record,'country12':countrys})
def create_city(request):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('record1')
    else:
        form = CityForm()
    return render(request, 'create_city.html', {'form': form})
def create_country(request):
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('record1')
    else:
        form = CountryForm()
    return render(request, 'create_country.html', {'form': form})
def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('record1')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})
    
def edit_city(request, id):
    city = get_object_or_404(City, id=id)  # Safely fetch the city
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            # Fetch related records only after saving
            students = Student.objects.all()
            city_record = City.objects.all()
            return render(request, 'record.html', {'stud12': students, 'city12': city_record})
    else:
        form = CityForm(instance=city)
    return render(request, 'edit_city.html', {'city': city,'form': form})
def delete_city(request, id):
    students = Student.objects.all()
    city_record = City.objects.all()
    city = City.objects.get(id=id)
    city.delete()
    return render(request, 'record.html', {'stud12': students, 'city12': city_record})
    

def delete_user(request, id):
    students = Student.objects.all()
    city_record = City.objects.all()
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
    context = {'stud12': students, 'city12': city_record}
    return render(request, 'record.html', context)




def edit_students(request, id):
    student = get_object_or_404(Student, id=id)  # Safely fetch the student
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Fetch related records only after saving
            students = Student.objects.all()
            city_record = City.objects.all()
            return render(request, 'record.html', {'stud12': students, 'city12': city_record})
    else:
        form = StudentForm(instance=student)

    # Include all necessary context for the template
    return render(request, 'edit_student.html', {'form': form, 'student': student})
def view_django(request):

    return render(request,'django.html',{})



def view_hello(request):

    return render(request,'hello.html',{})




def view_hello_20(request):   

    return render(request,'hello-20.html',{})



def view_record(request):

    stud_record = Student.objects.all()
    city_record = City.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'city12':city_record})


       # return render_to_response('courtcase/report_display.html', {'entry_list': q, 'entry_list1': q1,})


    # return render_to_response('hello.html', {'entry_list': q, 'entry_list1': q1,})





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# Note that once we’ve done this in all these views, we no longer need to import loader and Ht




# Create your views here.
