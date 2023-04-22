from django.shortcuts import render
from .models import Blog, Category, Course, Instructor, Lesson 

# Create your views here.
def homePage(request):
    blog = Blog.objects.all()[:5]
    return render(request, 'main/index.html', {'blog':blog})


def AllCourse(request):
    courses = Course.objects.all()

    params = {
        'course':courses,

    }


    return render(request, 'courses/course.html', params)

def Coursdetail(request, slug):
    course = Course.objects.get(slug = slug)

    params = {
        'course':course,

    }
    return render(request, 'courses/detail_course.html', params)

