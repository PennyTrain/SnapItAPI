from django.urls import path
from snaps import views

urlpatterns = [
    path('snaps/', views.SnapList.as_view()),
    path('posts/<int:pk>/', views.SnapDetail.as_view())
]