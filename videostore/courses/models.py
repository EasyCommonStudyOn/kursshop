from django.db import models
from PIL import Image
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField(
        default='default-slug')  # полное название url к определенному курсу- поле отвечает только за url
    title = models.CharField(max_length=120)
    description = models.TextField()  # без ограничения на длину текса для описания курса
    img = models.ImageField(default='default.png', upload_to='course_images')

    def __str__(self):  # при выводе обекта этого класа будет выведелено его title
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={
            'slug': self.slug})  # обращение к отслеживанию с urls. парамент подключаеться в значние slag во views


class Lesson(models.Model):
    slug = models.SlugField(default='default-slug') #Для создания своего url
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True) #как бы ссылка на запись в Course . delete - чтоб при удалении поле обнулялось
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):  # при выводе обекта этого класа будет выведелено его title
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={
            'slug': self.course.slug, 'lesson_slug':self.slug})  #
