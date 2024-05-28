from django.urls import path
from snaplikes import views
"""
This code defines URL patterns for listing all snap likes and for
retrieving, updating, or deleting a specific snap like by its
primary key, each mapped to corresponding views from the snaplikes module.
"""
urlpatterns = [
    path('snaplikes/', views.SnapLikeList.as_view()),
    path('snaplikes/<int:pk>/', views.SnapLikeDetail.as_view())
]
