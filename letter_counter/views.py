from collections import Counter
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def letter_counter(request):
	entered_word = request.POST.get('word')
	return HttpResponse(json.dumps(dict(Counter(entered_word))), content_type="application/json")
