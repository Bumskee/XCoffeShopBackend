# from rest_framework import viewsets
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.models import User

from .serializers import MenuesSerializer, UserSerializer
from .models import Menues

# class HeroViewSet (viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def menuesApi(request, id=0):
    if request.method=='GET':
        menues = Menues.objects.all()
        menues_serializer = MenuesSerializer(menues, many=True)
        return JsonResponse(menues_serializer.data, safe=False)
    elif request.method=='POST':
        menues_data = JSONParser().parse(request)
        menues_serializer = MenuesSerializer(data=menues_data)
        if menues_serializer.is_valid():
            menues_serializer.save()
            return JsonResponse("data added succesfully", safe=False)
        return JsonResponse("unable to add the data", safe=False)
    elif request.method=='PUT':
        menues_data = JSONParser().parse(request)
        menues = Menues.objects.get(menues_id=menues_data["menues_id"])
        menues_serializer = MenuesSerializer(Menues, data = menues_data)
        if menues_serializer.is_valid():
            menues_serializer.save()
            return JsonResponse("data was updated succesfully", safe=False)
        return JsonResponse("data was unable to be updated")
    elif request.method=="DELETE":
        menues = Menues.objects.get(menues_id=id)
        menues.delete()
        return JsonResponse("data deleted succesfully", safe = False)