# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import requests
from django.http import HttpResponse
import json

from bs4 import BeautifulSoup
import re

from .models import Treatment



def home(request):
    return HttpResponse('Epimedicator')

#def gettoken()
	
	
#	data=""
#	return data

def symptoms(request):
	
	""" This view is used to fetch all the symptoms from ApiMedic
		Args:
	  	  request: Request object
	
		Returns:
	  	  Returns list of symptoms with name and ids.
	"""
	formatvar='json'
	lang='en-gb'
#	token=gettoken()
	token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imtlc2hhdmtldmluMjIxQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTI5NSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjEwOCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiIxMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJCYXNpYyIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTgtMTAtMTAiLCJpc3MiOiJodHRwczovL2F1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1MzkxOTc3NTYsIm5iZiI6MTUzOTE5MDU1Nn0._xRskuGhdv-si1-I_x8P4NMLGHZHg0vvvW2Ik6CyNEk'
    	response = requests.get('https://healthservice.priaid.ch/symptoms?token='+str(token)+'&format'+str(formatvar)+'&language='+str(lang))
	
    	return HttpResponse(response)


def conditions(request):

	""" This view is used to fetch all the medical conditions from ApiMedic
		Args:
	  	  request: Request object
  
		Returns:
	  	  Returns list of medical conditions with issues and their specialization details.
	"""
	symptoms=request.GET.get('symptoms','[9]')
	gender=request.GET.get('gender','"male"')
	year_of_birth=request.GET.get('year_of_birth','1982')
#	token=gettoken()
	formatvar='json'
	lang='en-gb'		
	token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imtlc2hhdmtldmluMjIxQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTI5NSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjEwOCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiIxMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJCYXNpYyIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTgtMTAtMTAiLCJpc3MiOiJodHRwczovL2F1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1MzkyNDYyMzksIm5iZiI6MTUzOTIzOTAzOX0.SntuAYD2MvAdpVHHQICRjOKCGdOueGkflejjG7MJ-9U'	
	response = requests.get('https://healthservice.priaid.ch/diagnosis?symptoms='+str(symptoms)+'&gender='+str(gender)+'&year_of_birth='+str(year_of_birth)+'&token='+str(token)+'&format='+str(formatvar)+'&language='+str(lang))
	
	return HttpResponse(response)


def treatment(request):
	
	""" This view is used to fetch treatment for a given condition
		Args:
	  	  request: Request object
  
		Returns:
	  	  Returns string containing the treatment for the condition.
	"""

	issue=request.GET.get('issue_id','104')
	issue_condition=request.GET.get('issue_condition','Cephalalgia')	
	#issue_condition='Cephalalgia'
	#issue=104
	try:
		data=Treatment.objects.get(issue_id=issue)
	except Treatment.DoesNotExist:
		data=None
	if data:
		needed_treatment=data.treatment
	else: 
		data=get_treatment_options("a","b",issue, issue_condition)
		needed_treatment=data
		d=Treatment(issue_id=issue ,condition=issue_condition , treatment=needed_treatment)
		d.save()

	return HttpResponse(needed_treatment)


###########
def get_treatment_options(request, symptom_id, issue_id,disease_name):

		
	

        search_results = []
        search_url = 'https://www.google.co.in/search?q='+ disease_name + 'treatment'
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'lxml')
        for item in soup.select('.r a'):
            link = item.get('href').split('=')[1]
            link = link.split('&')[0]
            search_results.append(link)

        if search_results:
            treatement_methods = ''
            for link in search_results:
                treatment_details = requests.get(link)
                soup = BeautifulSoup(treatment_details.text, 'lxml')
                paragraphs = soup.findAll('p')

                for para in paragraphs:

                    if 'treatment'  in para.text:
                        treatement_methods += ' ' + para.text

                if treatement_methods:
                    return treatement_methods
                   












