from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 

from tutorials.models import Monuments
from tutorials.serializers import MonumentSerializer

from tutorials.models import LocalFood
from tutorials.serializers import LocalFoodSerializer

from rest_framework.decorators import api_view

    

@api_view(['GET', 'POST', 'DELETE'])
def monuments_list(request):
    if request.method == 'GET':
        monuments = Monuments.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            monuments = monuments.filter(title__icontains=title)
        
        monuments_serializer = MonumentSerializer(monuments, many=True)
        return JsonResponse(monuments_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        monument_data = JSONParser().parse(request)
        monuments_serializer = MonumentSerializer(data=monument_data)
        if monuments_serializer.is_valid():
            monuments_serializer.save()
            return JsonResponse(monuments_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(monuments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Monuments.objects.all().delete()
        return JsonResponse({'message': '{} Monuments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def monuments_detail(request, pk):
    try: 
        monuments = Monuments.objects.get(pk=pk) 
    except Monuments.DoesNotExist: 
        return JsonResponse({'message': 'The monuments does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        monuments_serializer = MonumentSerializer(monuments) 
        return JsonResponse(monuments_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        monuments_serializer = MonumentSerializer(monuments, data=tutorial_data) 
        if monuments_serializer.is_valid(): 
            monuments_serializer.save() 
            return JsonResponse(monuments_serializer.data) 
        return JsonResponse(monuments_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        monuments.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'DELETE'])
def localFoodList(request):
    if request.method == 'GET':
        localFood = LocalFood.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            localFood = localFood.filter(title__icontains=title)
        
        localFood_serializer = LocalFoodSerializer(localFood, many=True)
        return JsonResponse(localFood_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        localFood_data = JSONParser().parse(request)
        localFood_serializer = LocalFoodSerializer(data=localFood_data)
        if localFood_serializer.is_valid():
            localFood_serializer.save()
            return JsonResponse(localFood_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(localFood_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = LocalFood.objects.all().delete()
        return JsonResponse({'message': '{} LocalFood were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def localFoodDetail(request, pk):
    try: 
        monuments = LocalFood.objects.get(pk=pk) 
    except Monuments.DoesNotExist: 
        return JsonResponse({'message': 'The monuments does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        localFood_serializer = LocalFoodSerializer(monuments) 
        return JsonResponse(localFood_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        localFood_serializer = LocalFoodSerializer(monuments, data=tutorial_data) 
        if localFood_serializer.is_valid(): 
            localFood_serializer.save() 
            return JsonResponse(localFood_serializer.data) 
        return JsonResponse(localFood_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        monuments.delete() 
        return JsonResponse({'message': 'Local Food was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    