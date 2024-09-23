from django.shortcuts import render
from .models import Faculty, Kafedra, Group, Subject, Teacher, Student


def home_view(request):
    return render(request, 'home.html')


def faculty_view(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render(request, 'faculty.html', ctx)


def kafedra_view(request):
    kaferas = Kafedra.objects.all()
    ctx = {'kaferas': kaferas}
    return render(request, 'kafedra.html', ctx)


def group_view(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'group.html', ctx)


def subject_view(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subject.html', ctx)


def teacher_view(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teacher.html', ctx)


def student_view(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'student.html', ctx)
