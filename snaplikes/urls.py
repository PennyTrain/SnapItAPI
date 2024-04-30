from django.urls import path
from snaplikes import views

urlpatterns = [
    path('snaps/', views.SnapLikeList.as_view()),
    path('posts/<int:pk>/', views.SnapLikeDetail.as_view())
]