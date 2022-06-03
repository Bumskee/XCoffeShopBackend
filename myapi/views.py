# from rest_framework import viewsets
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .serializers import HeroSerializer
from .models import Hero

# class HeroViewSet (viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

# Create your views here.

@csrf_exempt
def herosApi(request, id=0):
    if request.method=='GET':
        heros = Hero.objects.all()
        heros_serializer = HeroSerializer(heros, many=True)
        return JsonResponse(heros_serializer.data, safe=False)
    elif request.method=='POST':
        heros_data = JSONParser().parse(request)
        heros_serializer = HeroSerializer(data=heros_data)
        if heros_serializer.is_valid():
            heros_serializer.save()
            return JsonResponse("data added succesfully", safe=False)
        return JsonResponse("unable to add the data", safe=False)
    elif request.method=='PUT':
        heros_data = JSONParser().parse(request)
        heros = Hero.objects.get(heros_id=heros_data["heros_id"])
        heros_serializer = HeroSerializer(heros, data = heros_data)
        if heros_serializer.is_valid():
            heros_serializer.save()
            return JsonResponse("data was updated succesfully", safe=False)
        return JsonResponse("data was unable to be updated")
    elif request.method=="DELETE":
        heros = Hero.objects.get(heros_id=id)
        heros.delete()
        return JsonResponse("data deleted succesfully", safe = False)