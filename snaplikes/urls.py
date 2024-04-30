from django.urls import path
from snaplikes import views

urlpatterns = [
    path('snaplikes/', views.SnapLikeList.as_view()),
    path('snaplikes/<int:pk>/', views.SnapLikeDetail.as_view())
]