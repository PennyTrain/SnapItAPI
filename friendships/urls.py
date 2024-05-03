from django.urls import path
from friendships import views


urlpatterns = [
    path('friendships/', views.SnapFriendshipList.as_view()),
    path('friendships/<int:pk>', views.SnapFriendshipDetail.as_view()),
]