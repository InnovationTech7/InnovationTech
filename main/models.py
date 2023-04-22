from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    text_intro = models.CharField(max_length=300)
    content = models.TextField()
    up_date = models.DateTimeField(auto_now=True)
    photo_article = models.ImageField(upload_to="photo")

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_info = models.CharField(max_length=200)


class Course(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Débutant'),
        ('Intermediate', 'Intermédiaire'),
        ('Advanced', 'Avancé')
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    prerequisites = models.TextField()
    target_audience = models.TextField()
    overview = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    student_count = models.PositiveIntegerField()
    quiz = models.TextField()
    categories = models.ManyToManyField('Category')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    photo_course = models.ImageField(upload_to="photo_course")
    unlimited_access = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

