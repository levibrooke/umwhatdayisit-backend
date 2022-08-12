from django.urls import path
from . import views

urlpatterns = [
  path('api/content/', views.ContentView.as_view()),
  path('api/content/<int:id>/', views.ContentView.as_view())
  ]