from django.contrib import admin
from .models import Faculty, Kafedra, Group, Subject, Teacher, Student

admin.site.register(Faculty)
list_display = ('name',)
search_fields = ('name',)

admin.site.register(Kafedra)
list_display = ('name',)
search_fields = ('name',)

admin.site.register(Group)
list_display = ('name', 'faculty')
search_fields = ('name',)

admin.site.register(Subject)
list_display = ('name', 'kafedra')
search_fields = ('name',)

admin.site.register(Teacher)
list_display = ('first_name', 'last_name', 'subject')
search_fields = ('first_name', 'last_name')

admin.site.register(Student)
list_display = ('first_name', 'last_name', 'kafedra', 'group')
search_fields = ('first_name', 'last_name')
