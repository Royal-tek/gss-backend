from django.urls import path
from .views import StudentView,ParentView, TeacherView
urlpatterns = [
    path('student/', StudentView.as_view()),
    path('parent/', ParentView.as_view()),
    path('teacher/', TeacherView.as_view()),
]
