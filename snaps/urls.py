from django.urls import path
from snaps import views
"""
This code defines URL patterns for listing all
snaps and for retrieving, updating, or deleting
a specific snap by its primary key, each mapped
to corresponding views from the snaps module.
"""

urlpatterns = [
    path('snaps/', views.SnapList.as_view()),
    path('snaps/<int:pk>/', views.SnapDetail.as_view())
]
