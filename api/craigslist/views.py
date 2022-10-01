import imp
import json
import requests
from craigslist.utils.url_utils import create_url
from craigslist.utils.verification_utils import verify_request
from craigslist.utils.html_utils import create_response_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vehicles(request):
    if verify_request(request.body):
        url = create_url(request.body)
        html = requests.get(url).text
        response_dict = create_response_dict(html=html)
        return HttpResponse(url)
    else: 
        return HttpResponse(status=400)
