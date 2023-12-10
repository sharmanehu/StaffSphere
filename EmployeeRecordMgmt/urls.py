"""
URL configuration for EmployeeRecordMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from employee.views import *
from .views import logistic_regression_predict
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  #admin_page
    path('',index,name='index'),  #first page
    path('registration' ,registration, name='registration'), #resgister for signup
    path('emp_login',emp_login, name='emp_login'), #loginpage
    path('emp_home', emp_home, name='emp_home'), #homepage
    path('profile', profile, name='profile'),  #profile page
    path('logout', Logout, name='logout'),#logout page
    path('admin_login', admin_login, name='admin_login'),#admin login
    path('my_experience', my_experience, name='my_experience'),#experience page
    path('edit_myexperience', edit_myexperience, name='edit_myexperience'),#experience edit
    path('my_education', my_education, name='my_education'),  # education page
    path('edit_myeducation', edit_myeducation, name='edit_myeducation'),  # education edit
    path('change_password', change_password, name='change_password'), #changepassword page
    path('admin_home', admin_home, name='admin_home'), #admin_homepage
    path('change_passwordadmin', change_passwordadmin, name='change_passwordadmin'),  # changepasswordadmin page
    path('all_employee', all_employee, name='all_employee'),
    path('edit_education/<int:pid>', edit_education, name='edit_education'),
    path('edit_experience/<int:pid>', edit_experience, name='edit_experience'),
    path('logistic_regression_predict/', logistic_regression_predict, name='logistic_regression_predict'),
    path('employee', include('employee.urls')),
]
