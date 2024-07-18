from django.urls import path 
from .views import home, about, services, why_choose, teachers


urlpatterns = [
    path('', view=home.as_view(), name='home'),
    path('about/<int:pk>/', view=about.as_view(), name='about'),
    path('services/<int:pk>/', view=services.as_view(), name='services'),
    path('why/', view=why_choose.as_view(), name='why'),
    path('team/',view=teachers.as_view(),name='team'),
]