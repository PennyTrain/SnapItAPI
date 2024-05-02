from django.urls import path
from snap_comments import views

urlpatterns = [
    path('snapcomments/', views.SnapCommentList.as_view()),
    path('snapcomments/<int:pk>', views.SnapCommentDetail.as_view()),
]