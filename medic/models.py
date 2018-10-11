# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Treatment(models.Model):
	issue_id = models.IntegerField()	
	condition = models.CharField(max_length=255)
	treatment = models.TextField()
