from django.shortcuts import render, redirect
from .models import Employee, Gender, Department

# Create your views here.


def home(request):
    return render(request, 'dashboard.html')


def view_all(request):
    employees = Employee.objects.all()
    return render(request, 'view_all.html', context={'employees': employees})


def add_emp(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        dob = request.POST['dob']
        gender = int(request.POST['gender'])
        ph_no = request.POST['ph_no']
        email = request.POST['email']
        dept = int(request.POST['dept'])
        position = request.POST['position']
        salary = int(request.POST['salary'])
        employee = Employee(name=name, emp_id=emp_id, dob=dob, gender_id=gender,
                            ph_no=ph_no, email=email, dept_id=dept, position=position, salary=salary)
        employee.save()
        return redirect(view_all)
    else:
        return render(request, 'add_emp.html')


def update_emp(request):
    if request.method == 'POST':
        if request.POST['emp_id']:
            if Employee.objects.filter(emp_id=request.POST['emp_id']).exists():
                employee = Employee.objects.get(pk=request.POST['emp_id'])
                employees = [employee]
            else:
                employees = []
        elif request.POST['name']:
            if Employee.objects.filter(name__icontains=request.POST['name']).exists():
                employees = Employee.objects.filter(
                    name__icontains=request.POST['name'])
            else:
                employees = []
        else:
            employees = Employee.objects.all()
        return render(request, 'update_emp.html', context={'employees': employees})
    else:
        employees = Employee.objects.all()
        return render(request, 'update_emp.html', context={'employees': employees})


def update_form(request, id=0):
    if id:
        if Employee.objects.filter(emp_id=id).exists():
            employee = Employee.objects.get(pk=id)
            return render(request, 'update_form.html', context={'employee': employee})
        else:
            return render(request, 'update_emp.html', context={'employees': []})
    else:
        return redirect(update_emp)


def remove_emp(request):
    if request.method == 'POST':
        if request.POST['emp_id']:
            if Employee.objects.filter(emp_id=request.POST['emp_id']).exists():
                employee = Employee.objects.get(pk=request.POST['emp_id'])
                employees = [employee]
            else:
                employees = []
        elif request.POST['name']:
            if Employee.objects.filter(name__icontains=request.POST['name']).exists():
                employees = Employee.objects.filter(
                    name__icontains=request.POST['name'])
            else:
                employees = []
        else:
            employees = Employee.objects.all()
        return render(request, 'remove_emp.html', context={'employees': employees})
    else:
        employees = Employee.objects.all()
        return render(request, 'remove_emp.html', context={'employees': employees})


def delete_emp(request, id=0):
    if request.method == 'POST':
        employees = list(request.POST)
        if employees[1] == 'all':
            Employee.objects.all().delete()
        else:
            for i in range(1,len(employees)):
                Employee.objects.get(emp_id=employees[i]).delete()
    return redirect(remove_emp)
    # if id:
    #     if Employee.objects.filter(emp_id=id).exists():
    #         employee = Employee.objects.get(pk=id)
    #         employee.delete()
    #     return redirect(remove_emp)
    # else:
    #     return redirect(remove_emp)
