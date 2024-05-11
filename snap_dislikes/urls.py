from django.urls import path
from snap_dislikes import views

urlpatterns = [
    path('snapdislikes/', views.SnapDislikeList.as_view()),
    path('snapdislikes/<int:pk>/', views.SnapDislikeDetail.as_view())
]