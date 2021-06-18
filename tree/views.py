from django.shortcuts import render, redirect
from .models import Employees
from .utils import *
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

LIM = 50
NO_USER = 'Это не пользователь'
LOGIN = 'Авторизуйтесь login: admin  pass: 12345678'
NO_LOGIN = 'Вы не авторизованы login: admin  pass: 12345678'

def emp_tree(request, template_name='emp_tree.html'):

    if request.method == 'GET':
        emps = Employees.objects.filter(level__lte=1)
        emps = emps.order_by('-rght').all()
        count_all = Employees.objects.count()
        data = {
            'employees': emps,
            'count_all': count_all
        }
        return render(request, template_name, context=data)

def not_authenticated(request, template_name='not_authenticated.html'):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('emp_table_url'))   # success page
        else:
            data = {
                'text': NO_USER
            }
            return render(request, template_name, context=data)
    else:
        data = {
            'text': LOGIN
        }
        return render(request, template_name, context=data)


@csrf_protect
def ajax_dragdrop(request):

    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        new_parent_id = request.POST['new_parent']
        new_parent = Employees.objects.get(id=new_parent_id)
        emp = Employees.objects.get(id=id)
        old_par_id = emp.parent_id
        old_par = Employees.objects.get(id=old_par_id)
        childrens_count = old_par.get_children().count()
        emp.move_to(new_parent)
        return JsonResponse({'old_par_id': old_par_id, 'childrens_count': childrens_count})

    return render(request, "404.html")

@csrf_protect
def ajax_tree(request):

    if request.method == 'POST':

        id = request.POST['id']
        emps = Employees.objects.filter(parent_id=id).all()

        return json_data_tree(emps)

    return render(request, "404.html")  # if some one try to get to the page

