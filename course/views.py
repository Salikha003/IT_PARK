from django.shortcuts import render, redirect
from django.views import View
from .forms import SubscriberForm
from .models import CoursePage, ServicePage, Why_Choose, Teachers, Customer_reviews


class home(View):
    def get(self, request):
        courses_objects = CoursePage.manager.all()
        courses_object = CoursePage.manager.all()
        services_objects = ServicePage.objects.all()
        why_choose_us = Why_Choose.objects.all()
        teacher = Teachers.objects.all()
        customer_reviews = Customer_reviews.objects.all()
        form = SubscriberForm()

        context = {
            'courses_objects' : courses_objects,
            'courses_object' : courses_object,
            'services_objects' : services_objects,
            'why_choose_us' : why_choose_us,
            'teacher' : teacher,
            'customer_reviews' : customer_reviews,
            'form' : form,
        }

        
        return render(request=request, template_name='index.html', context=context)
    

    def post(self, request):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        return render(request, 'index.html', {'form': form})
    
    

class services(View):
    def get(self, request, pk):
        service_object = ServicePage.objects.get(pk=pk)
        form = SubscriberForm()

        context = {
            'service_object' : service_object,
            'form' : form,
        }

        return render(request=request, template_name='service.html', context=context)
    

    def post(self, request):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        return render(request, 'service.html', {'form': form})
    

class about(View):
    def get(self, request, pk):
        about_objects = CoursePage.objects.get(pk=pk)
        form = SubscriberForm()

        context = {
            'about_objects' : about_objects,
            'form' : form,
        }

        return render(request=request, template_name='about.html', context=context)
    


    def post(self, request):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        return render(request, 'about.html', {'form': form})


class why_choose(View):
    def get(self, request):
        why_choose = Why_Choose.objects.all()
        

        context = {
            'why_choose' : why_choose,
        }

        return render(request=request, template_name='why.html', context=context)


class teachers(View):
    def get(self, request):
        teacher = Teachers.objects.all()

        context = {
            'teacher' : teacher,
        }

        return render(request=request, template_name='team.html', context=context)



