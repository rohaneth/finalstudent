from django.shortcuts import render, get_object_or_404, redirect
from student.models import Country, City, Student, Company,User
from .forms import StudentForm,CityForm,CountryForm  # Replace with your form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the menu page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('index')  

def home(request):
    return render(request, 'index.html')

@login_required
def edit_country(request,pk):
    country = Country.objects.filter(country_name=pk)
    if country.exists():
        country = Country.objects.get(country_name=pk)
        form = CountryForm(instance=country)
        if request.method == 'POST':
            form = CountryForm(request.POST, instance=country)
            if form.is_valid():
                form.save()
                return redirect('countryedit')
    else:
        form = CountryForm()
    return render(request, 'edit_country.html', {'form': form, 'country': country})
@login_required
def editstudent(request):
    student = Student.objects.all()
    return render(request, 'editstudent.html', {'student': student})
@login_required
def editcity(request):
    city = City.objects.all()
    return render(request, 'editcity.html', {'city': city})
@login_required
def editcountry(request):
    country = Country.objects.all()
    return render(request, 'editcountry.html', {'country': country})


@login_required
def studentdisplay(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'student_name')  # Default sorting by student_name
    student = Student.objects.all()

    
    if search_query:
        student = student.filter(
            Q(student_name__icontains=search_query) |
            Q(city__city_name__icontains=search_query) |  # Adjust if your City model has a name field
            Q(branch__icontains=search_query) |
            Q(education__icontains=search_query) |
            Q(experience__icontains=search_query)
        ).order_by(sort_by)
    
    if sort_by == 'student_name':
        student = student.order_by('student_name')
    elif sort_by == 'city':
        student = student.order_by('city__city_name')  # Adjust if your City model has a name field
    elif sort_by == 'branch':
        student = student.order_by('branch')
    elif sort_by == 'education':
        student = student.order_by('education')
    elif sort_by == 'experience':
        student = student.order_by('experience')

    return render(request, 'displaystudents.html', { 'student':student})
@login_required
def countrydisplay(request):
    country = Country.objects.all()
    return render(request, 'displaycountry.html', {'country':country})
@login_required
def citydisplay(request):
    city  = City.objects.all()
    country = Country.objects.all()
    return render(request, 'displaycity.html', {'city':city,'country':country})
@login_required
def city(request):
    return render(request, 'cityindex.html', {})
@login_required
def country(request):
    return render(request, 'countryindex.html', {})
@login_required
def student(request):
    return render(request, 'studentindex.html', {})

def index(request):
    return render(request, 'index.html', {})
@login_required

def deletestudent(request):
    students = Student.objects.all()
    city_record = City.objects.all()
    return render(request, 'deletestudent.html', {'student': students, 'city': city_record})
@login_required
def deletecountry(request):
    country = Country.objects.all()
    return render(request, 'deletecountry.html', {'country': country})
@login_required
def deletecity(request):
    city = City.objects.all()
    return render(request, 'deletecity.html', {'city': city})
@login_required
def delete_country(request, pk):
    students = Student.objects.all()
    city_record = City.objects.all()
    countrys = Country.objects.all()
    #delete conuntry where countryneme is pk
    countrys = Country.objects.filter(country_name=pk)
    if countrys.exists():
        countrys.delete()
    return redirect('countrydelete')
@login_required
def create_city(request):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('citydisplay')
    else:
        form = CityForm()
    return render(request, 'create_city.html', {'form': form})

@login_required
def create_country(request):
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('countrydisplay')
    else:
        form = CountryForm()
    return render(request, 'create_country.html', {'form': form})
@login_required
def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('studentdisplay')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})
@login_required
def edit_city(request, id):
    city = get_object_or_404(City, id=id)  # Safely fetch the city
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            # Fetch related records only after saving
            students = Student.objects.all()
            city_record = City.objects.all()
            return redirect('cityedit')
    else:
        form = CityForm(instance=city)
    return render(request, 'edit_city.html', {'city': city,'form': form})
@login_required
def delete_city(request, id):
    students = Student.objects.all()
    city_record = City.objects.all()
    city = City.objects.get(id=id)
    city.delete()
    return redirect('citydelete')
    
@login_required
def delete_student(request, id):
    students = Student.objects.all()
    city_record = City.objects.all()
    
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
    context = {'student': students, 'city': city_record}
    return render(request, 'deletestudent.html', context)


@login_required
def edit_students(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentedit')
            # Fetch related records only after saving
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
