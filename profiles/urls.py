from django.urls import path
from profiles import views
"""
This code defines URL patterns for the profiles app,
mapping the root 'profiles/' to the ProfileList view
for listing and creating profiles. It also maps
'profiles/int:pk/' to the ProfileDetail view for
retrieving, updating, and deleting individual profiles
based on their primary key.
"""


urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
