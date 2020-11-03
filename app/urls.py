from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/<int:student_id>/', views.StudentView, name='student'),
    path('assignment/<int:assignment_id>', views.AssignmentView, name="assignment")
    # path('student/', views.StudentView.as_view(), name='student')
]