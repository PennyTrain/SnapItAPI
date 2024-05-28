from django.urls import path
from friendships import views

"""
This code defines URL patterns for the friendships app,
mapping the root 'friendships/' to the
SnapFriendshipList
view and 'friendships/int:pk'
to the SnapFriendshipDetail view.
"""

urlpatterns = [
    path('friendships/', views.SnapFriendshipList.as_view()),
    path('friendships/<int:pk>', views.SnapFriendshipDetail.as_view()),
]
