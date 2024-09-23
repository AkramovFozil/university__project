from django.urls import path
from .views import home_view, faculty_view, kafedra_view, group_view, subject_view, teacher_view, student_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('faculties/', faculty_view, name='faculty_view'),
    path('kafedras/', kafedra_view, name='kafedra_view'),
    path('groups/', group_view, name='group_view'),
    path('subjects /', subject_view, name='subject_view'),
    path('teachers/', teacher_view, name='teacher_view'),
    path('students/', student_view, name='student_view'),

]
