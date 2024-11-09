from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from employee.models import EmployeeDetail, EmployeeExperience, EmployeeEducation


def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn =  request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user = user,empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            error="no"
        except:
            error="yes"
    return render(request,'registration.html',locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:  #if directly open
        return redirect('emp_login')
    return render(request,'emp_home.html')

def Logout(request):
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"

    return render(request,'profile.html',locals())

#admin login function
def admin_login(request):
    return render(request,'admin_login.html')

#experience function
def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    return render(request,'my_experience.html',locals())

#edit_experience function
def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2salary = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_myexperience.html',locals())



#education function
def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    try :

        education = EmployeeEducation.objects.get(user=user)
    except:
        print("users")
    print(user)
    return render(request,'my_education.html',locals())


#edit myeducation function
def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    try:

        education = EmployeeEducation.objects.get(user=user)
    except:
        print("users")
    print(user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclgra = request.POST['schoolclgra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassing = yearofpassing
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclgra = schoolclgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_myeducation.html',locals())

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""

    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'change_password.html',locals())



def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
              login(request,user)
              error = "no"
            else:
              error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html',locals())

from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeExperience

import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import EmployeeExperience

@login_required
def admin_home(request):
    experience_labels = ['0-1 years', '1-3 years', '3-5 years', '5+ years']
    experience_counts = [0] * len(experience_labels)

    # Helper function to extract numeric value from duration string
    def extract_years(duration):
        match = re.search(r'(\d+)', duration)
        return int(match.group(1)) if match else 0

    # Count employees in each experience category
    for experience in EmployeeExperience.objects.all():
        if experience.company1duration:
            years = extract_years(experience.company1duration)
            if years <= 1:
                experience_counts[0] += 1
            elif years <= 3:
                experience_counts[1] += 1
            elif years <= 5:
                experience_counts[2] += 1
            else:
                experience_counts[3] += 1

    return render(request, 'admin_home.html', {
        'experience_labels': experience_labels,
        'experience_counts': experience_counts,
    })



#change password admin function
def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""

    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'change_passwordadmin.html',locals())


#list of employees in admin function
def all_employee(request):
    if not request.user.is_authenticated:  #data of all employee
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request,'all_employee.html',locals())

#admin side edit education function
def edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclgra = request.POST['schoolclgra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassing = yearofpassing
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclgra = schoolclgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_education.html',locals())


#admin side edit experience function
def edit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2salary = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_experience.html',locals())





