from django.urls import path
from snap_dislikes import views
"""
This code defines two URL patterns for handling snap
dislike-related views: one for listing all snap dislikes
and one for retrieving, updating, or deleting a specific
snap dislike by its primary key. Each URL pattern is mapped
to a corresponding view class from the snap_dislikes.views
module.
"""

urlpatterns = [
    path('snapdislikes/', views.SnapDislikeList.as_view()),
    path('snapdislikes/<int:pk>/', views.SnapDislikeDetail.as_view())
]
