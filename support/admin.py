# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from dal import autocomplete
from .models import Course, Student



class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        widgets = {
            'course': autocomplete.ModelSelect2(url='course-autocomplete')
        }


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ('firstName', 'course', 'lastName', 'rollNumber')
    search_fields = ['course__courseName',]

admin.site.register(Course)
admin.site.register(Student, StudentAdmin)