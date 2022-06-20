from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages

def index(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request, "index.html", context)

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            new_course = Course.objects.create(
                name = request.POST['name'],
                description = request.POST['desc'],
            )
            new_course.save()
            return redirect('/')

def remove_course(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course' : course,
    }
    return render(request, "delete.html", context)

def delete_course(request, id):
    del_course = Course.objects.get(id=id)
    del_course.delete()
    return redirect('/')