# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from dal import autocomplete

from .models import Course


class CourseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Course.objects.all()
        if self.q:
            qs = qs.filter(courseName__icontains=self.q)
        return qs
