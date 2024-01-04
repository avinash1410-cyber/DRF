from django.http import JsonResponse,HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
import json






def api_response(request):
    model_data=Product.objects.all().first()
    data=model_to_dict(model_data,fields=['id','name'])
    json_data=json.dumps(data)
    return HttpResponse(json_data)