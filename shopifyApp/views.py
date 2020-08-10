from django.shortcuts import render
from . import constants
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import json


def getProduct(request):
	try:
		products_list = makeRequest(constants.product_string, 'GET', 'json')
		return JsonResponse(products_list)
	except Exception as e:
		print(e)
		return JsonResponse({"error":str(e)})


def orderProduct(request):
	try:
		if(request.method == 'GET'):
			makeRequest(constants.order_string, 'GET', json)
			order_list = makeRequest(constants.order_string, 'GET', 'string')
			print("LOOK HERE",type(order_list))
			return JsonResponse(order_list, safe=False)

		elif(request.method == 'POST'):
			product_id = request.POST.get('product_id')
			quantity = int(request.POST.get('quantity'))
			createOrder(product_id, quantity)

			updateInventory(product_id, quantity)	
	except Exception as e:
		print(e)
		return JsonResponse({"error":str(e)})

def createOrder(product_id, quantity):
	try:
		pass
	except Exception as e:
		print(e)


def updateInventory(product_id, quantity):
	try:
		pass
	except Exception as e:
		print(e)


def makeRequest(resource_identifier, request_type, response_type):
	try:
		url = constants.BaseURL +  resource_identifier + '.json'
		response = ''
		if(request_type == 'GET'):
			response = requests.get(url)
		elif(request_type == 'POST'):
			response = requests.POST(url)

		if(response_type == 'json'):
			return json.loads(response.text)
		else:
			return response.text	
	except Exception as e:
		print(e)
		return JsonResponse({"error":str(e)})
