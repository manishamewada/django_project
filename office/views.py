from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'office/index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context={
        'emps':emps 
    }
    return render(request,'office/view_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=request.POST['salary']
        bouns=int(request.POST['bouns'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        dept=int(request.POST['dept'])

        em=Employee(first_name=first_name,last_name=last_name,salary=salary,bouns=bouns,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        em.save()
        return HttpResponseRedirect("/")
    elif request.method=="GET":
        return render(request,'office/add_emp.html')
    else:
           return HttpResponse('unsuccessfull')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            empremoved = Employee.objects.get(id=emp_id)
            empremoved.delete()
            return HttpResponse("delete successfully")
        except:
            return HttpResponse('please enter a valid id')
    emps=Employee.objects.all()
    context={'emps':emps}

    return render(request,'office/remove_emp.html',context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context={'emps':emps }
        return render(request,'office/view_emp.html',context)
    elif request.method=="GET":
        return render(request,'office/filter_emp.html')
    else:
        return HttpResponse('an exception occured!')
