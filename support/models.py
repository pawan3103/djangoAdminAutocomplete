# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
	courseName = models.CharField(max_length=254)
	fees = models.DecimalField(max_digits=20, decimal_places=2)

	def __str__(self):
		return self.courseName


class Student(models.Model):
	firstName = models.CharField(max_length=254)
	lastName = models.CharField(max_length=254)
	rollNumber = models.CharField(max_length=254, unique=True)
	course = models.ForeignKey(Course)


