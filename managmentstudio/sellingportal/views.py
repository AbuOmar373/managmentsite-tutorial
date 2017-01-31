from django.shortcuts import render
from django.http import HttpResponse

from sellingportal import models

def Index(request):
    context={'name':'Manei',
            'age':26,
            'jobs':['eng', 'dev', 'lecture']
            }
    return render(request, 'index.html', context)

    #return HttpResponse('welcome to index page')

def Student(request):
    students=models.Student.objects.all()
    context ={
        'students':students
    }
    return render(request, 'students.html', context)


def StudenDegree(request,student_id):
    degrees = models.Degree.objects.filter(student_id=student_id)
    context = {
        'degrees': degrees
    }
    return render(request, 'degrees.html', context)