from django.urls import path
from tracker.views import interview_list, show_interview, create_interview, update_interview

urlpatterns = [
    path("", interview_list, name="interview_list"),
    path("<int:id>/", show_interview, name="show_interview"),
    path("create/", create_interview, name='create_interview'),
    path("<int:id>/edit/", update_interview, name='update_interview'),
 ]
