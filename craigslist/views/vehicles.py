import time
from craigslist.utils.url_utils import create_url
from craigslist.utils.verification_utils import verify_request
from craigslist.utils.html_utils import create_response_dict
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from api.globals import get_global_driver

class VehiclesView(View):
    def post(self, request):
        if verify_request(request.body):
            url = create_url(request.body)
            global_driver = get_global_driver(start_url=url, args=["--headless"])
            time.sleep(1)
            html = global_driver.driver.page_source.encode()
            response_dict = create_response_dict(html=html)
            return JsonResponse(response_dict)
        else: 
            return HttpResponse(status=400)
