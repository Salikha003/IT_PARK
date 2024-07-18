from django.contrib import admin
from .models import CoursePage, ServicePage, Why_Choose, Teachers, Customer_reviews, Subscriber

@admin.register(CoursePage)
class CoursePageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Why_Choose)
class Why_ChooseAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')


@admin.register(Customer_reviews)
class CustomerReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    
    
    
    
    