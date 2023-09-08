from django.db import models
from PIL import Image

class Course(models.Model):
    slug = models.SlugField(default='default-slug') # полное название url к определенному курсу- поле отвечает только за url
    title = models.CharField(max_length=120)
    description = models.TextField() # без ограничения на длину текса для описания курса
    img = models.ImageField(default='default.png', upload_to='course_images')

    def __str__(self): # при выводе обекта этого класа будет выведелено его title
        return self.title




