import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import requests
from django.http import JsonResponse, HttpResponse
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """drf api view"""
   
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)
    





















# -------------------------2------------------------

 # data=request.data
    # instance = Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     # data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
    #   data = ProductSerializers(instance).data


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data = model_to_dict(model_data, fields = ['id', 'title', 'price'])
#         # json_data_str = json.dumps(data)
#         # data["id"] = model_data.id
#         # data["title"] = model_data.title
#         # data["content"] = model_data.content
#         # data["price"] = model_data.price
#         # this is serailization
#         # model instances 
#         # tuen a python a dict 
#         # return JSON to my client 

#     # return HttpResponse(json_data_str, headers={"content-type":"application/json"})
#     # return HttpResponse(data, headers={"content-type":"application/json"})
#     return JsonResponse(data)


# -------------------------1------------------------


# def api_home(request, *args, **kwargs):
#     # request -> HttpResponse django instance
#     # body = requests.body  byte sptring of json data
#     # print(dir(request))
#     print(request.GET)
#     print(request.POST)
#     body= request.body #byte string of json data
#     data={}
#     try:
#         data = json.loads(body) #string of json to python dict
#     except:
#         pass
#     print(data)
#     print(request.headers)
#     # json.dumps(dict(request.headers))
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
#     # print(data.keys)
#     # print(data)
#     # data['headers'] = request.headers  #request.META ->
#     # # data['params'] 
#     # # data['headers'] = dict(request.headers)
#     # # print(request.headers)
#     # data['content_type'] = request.content_type
#     # return JsonResponse(data)
#     # return JsonResponse({"message": "hi hello this is your api message"})

#     # return JsonResponse({"message": "this is a api response"})