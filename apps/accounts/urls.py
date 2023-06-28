from django.urls import path
from .views import TeacherRegistrationView, TeacherLoginView, TeacherLogoutView, CreateStudentView

urlpatterns = [
    path('register/', TeacherRegistrationView.as_view(), name='register'),
    path('login/', TeacherLoginView.as_view(), name='login'),
    path('logout/', TeacherLogoutView.as_view(), name='logout'),
    path('add-student/', CreateStudentView.as_view(), name='add_student')
]
