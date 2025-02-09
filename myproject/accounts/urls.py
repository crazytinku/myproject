from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.custom_login,name="login"),
    path("dashboard/",views.dashboard, name="dashboard"), 
    path('mark-attendance/', views.todays_attendance, name='todays_attendance'),
]

  # Ensure this template exists