from django.shortcuts import render
from django.http import HttpResponse
def Index(request):
    context={'name':'Manei',
            'age':26,
            'jobs':['eng', 'dev', 'lecture']
            }
    return render(request, 'index.html', context)

    #return HttpResponse('welcome to index page')

def Student(request):
    return HttpResponse('welcome to Student page')


def StudenDegree(request,student_id):
    return HttpResponse('welcome to Degree page you id:'+ student_id)