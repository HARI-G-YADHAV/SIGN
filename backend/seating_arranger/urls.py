from django.urls import path

from . import views


urlpatterns = [
    path('generate-seating-plan/', views.generate_seating_plan, name='generate-seating-plan'),
    path('generate-seating-plan2/', views.generate_seating_plan2, name='generate-seating-plan2'),
    path('generate-seating-plan3/', views.generate_seating_plan3, name='generate-seating-plan3'),
    path('generate-seating-plan4/', views.generate_seating_plan4, name='generate-seating-plan4'),
]
