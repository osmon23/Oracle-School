from django.urls import path

from .views import GradeView, CreateGradeView, StudentDetailView, StudentEditView, StudentDeleteView

urlpatterns = [
    path('', GradeView.as_view(), name='index'),
    path('create-grade/', CreateGradeView.as_view(), name='create_grade'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('student/<int:pk>/update/', StudentEditView.as_view(), name='update_student'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),
]
