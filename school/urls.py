"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from teacher import views as t
from student import views as s
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('error', t.error),
    path('welcome', t.welcome),
    path('pali', s.pali, name='pali'),
    path('palin', s.palin),
    path('home', s.home, name='home'),
    path('calc', s.calc, name='calc'),
    path('cal', s.cal),
    path('perfect', s.perfect, name='perfect'),
    path('per', s.per),
    path('fibo', s.fibo, name='fibo'),
    path('fib', s.fib),
    path('', s.login,name='login'),
    path('adlogin', s.adlogin),
    path('login',s.login,name='login'),
    path('regis', t.register, name='register'),
    path('reg', t.reg, name=''),
    path('viewcustomers', t.viewcustomers, name='viewcustomers'),
    path('del_cust',t.del_cust,name='del_cust'),
    path('edit_cust',t.edit_cust,name='edit_cust'),
    path('edi_cust',t.edi_cust,name='edi_cust'),
    path('tea_home',t.tea_home,name='tea_home'),
    
    
    # Teacher and Student Details
    path('teacherdetails',t.teacherdetails,name='teacherdetails'),
    path('studentdetails',s.studentdetails,name='studentdetails'),
    
    # Student Edit and Delete
    path('del_stu',s.del_stu,name='del_cust'),
    path('edit_stu',s.edit_stu,name='edit_stu'),
    path('edi_stu',s.edi_stu,name='edi_stu'),
    
    # Student Registration
    path('stu_home',s.stu_home,name='stu_home'),
    path('stud_registration',s.stud_registration,name='stud_registration'),
    path('stud_reg',s.stud_reg,name='stud_reg'),
    path('stu_view',s.stu_view,name="stu_view"),
    
    # Teacher view student
    path('stu_view_tea',t.stu_view_tea,name='stu_view_tea'),
    path('mark_register',t.mark_register,name='mark_register'),
    path('mark_reg',t.mark_reg,name='mark_reg'),
    
    # Student view marks
    path('stu_view_marks',s.stu_view_marks,name='stu_view_marks'),
    
    # Delete Marks
    path('del_mark',t.del_mark,name='del_mark'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
