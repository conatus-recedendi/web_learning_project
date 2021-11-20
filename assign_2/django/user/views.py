import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from pymongo import MongoClient

def read(request):
	client = MongoClient('mongodb://myUserAdmin:pwd@localhost:27017')
	db = client['baedalgeek_test']
	collection = db['Users']
	doc = collection.find().sort([("_id",-1)]).limit(1)[0]
	json = {
		"name": doc["name"],
		"age": doc["age"],
	}
	return JsonResponse(json, json_dumps_params={'ensure_ascii': True})