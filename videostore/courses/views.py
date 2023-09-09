from .models import Course, Lesson
from django.views.generic import ListView, DetailView  # для конкретной запысили на старинцах


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'  # имя шаьлона который будет обрабатывать эту страницу
    context_object_name = 'courses'  # с этой таблицы будет все вытягиваться
    ordering = ['-id']  # сортировка записей будет происхзодить в обратном порядке добавления

    def get_context_data(self, *, object_list=None, **kwargs):  # для передачи данных в сам шаблон
        ctx = super(HomePage, self).get_context_data(**kwargs)  # обращеие к ListView
        ctx['title'] = 'Главная страница сайта'  # передача этих елементов в сам шаблон
        return ctx


class CourseDetailPage(DetailView):
    model = Course  # какая таблица используеться
    template_name = 'courses/course-detail.html'  # какой шаблон используеться

    def get_context_data(self, *, object_list=None, **kwargs):  # для передачи данных в сам шаблон
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)  # обращеие к ListView
        ctx['title'] = Course.objects.filter(
            slug=self.kwargs[
                'slug']).first()  # перебрать все обьекты в этой модели с фильтром значения slug как и в url адресе. first - один обьект выбираем
        ctx['lessons'] = Lesson.objects.filter(course=ctx[
            'title']).order_by('number')  # название курса соответствует полю курс- вибрать все уроки курса название которого соответствуют странице на который мы сейчсас
        # print(ctx['lessons'].query) #отслеживание фильтра в терминале sql запросы
        return ctx

class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lessons-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):  # для передачи данных в сам шаблон
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)  # обращеие к ListView
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        # lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values()) # List чтоб не отражал QuerySet
        # ctx['title']=lesson[0]['title']
        # ctx['desc']=lesson[0]['description']
        # ctx['video']=lesson[0]['video_url'].split("=")[1]

        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        if lesson:
            ctx['title'] = lesson[0]['title']
            ctx['desc'] = lesson[0]['description']
            ctx['video'] = lesson[0]['video_url'].split("=")[1]
        else:
            # Обработка случая, когда урок не найден
            ctx['title'] = "Урок не найден"
            ctx['desc'] = "Описание урока не доступно"
            ctx['video'] = ""

        return ctx
