from django.contrib import admin
from .models import Blog, Lesson, Category, Course, Instructor
# Register your models here.
admin.site.register(Blog)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Instructor)