from django.db import models

# Create your models here.

class CoursePageManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status='active')


class CoursePage(models.Model):

    OPTIONS = (
        ('deactive', 'deactive'),
        ('active', 'active'),
    )

    photo = models.ImageField(upload_to='courses/', verbose_name='Rasmi')
    name = models.CharField(max_length=255, verbose_name='Nomi')
    about = models.TextField(verbose_name='Kurs haqida')
    status = models.CharField(max_length=255, choices=OPTIONS, default='deactive', verbose_name='Kurs holati')

    objects = models.Manager()
    manager = CoursePageManager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'CoursePage'
        managed = True
        verbose_name = 'Kurslar'
        verbose_name_plural = 'Kurslar'



class ServicePage(models.Model):
    photo = models.ImageField( upload_to='services/', verbose_name='Rasmi')
    name = models.CharField(max_length=255, verbose_name='Nomi')
    about = models.TextField(verbose_name='Service haqida')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Service_Page'
        managed = True
        verbose_name = 'Xizmatlar'
        verbose_name_plural = 'Xizmatlar'



class Why_Choose(models.Model):
    photo = models.ImageField(upload_to='why/')
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Why_Choose'
        managed = True
        verbose_name = 'Why_Choose'
        verbose_name_plural = 'Why_Choose'



class Teachers(models.Model):
    photo = models.ImageField(upload_to='team/', verbose_name='Rasmi')
    name = models.CharField(max_length=255, verbose_name='Ism, Familiyasi')
    about = models.TextField(verbose_name='Haqida')
    telegram = models.URLField(max_length=200, verbose_name='Telegram akkaunt linki')
    instagram = models.URLField(max_length=200, verbose_name='Instagram akkaunt linki')
    github = models.URLField(max_length=200, verbose_name='Github akkaunt linki')
    

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'Teachers'
        managed = True
        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers'



class Customer_reviews(models.Model):
    img = models.ImageField(upload_to='reviews/', verbose_name='Rasm')
    name = models.CharField(max_length=255, verbose_name='Kompaniya nomi')
    reviews = models.TextField(verbose_name='Fikrlar')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Customer_Reviews'
        managed = True
        verbose_name = 'MIjozlar fikri'
        verbose_name_plural = 'MIjozlar fikri'



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'Subscriber'
        managed = True
        verbose_name = 'Obunachilar'
        verbose_name_plural = 'Obunachilar'

    