from django.urls import path
from snap_comments import views
"""
The code defines two URL patterns for handling snap
comment-related views: one for listing all snap
comments and one for retrieving, updating, or deleting
a specific snap comment by its primary key. Each URL
pattern is mapped to a corresponding view class from
the snap_comments.views module.
"""


urlpatterns = [
    path('snapcomments/', views.SnapCommentList.as_view()),
    path('snapcomments/<int:pk>/', views.SnapCommentDetail.as_view()),
]
