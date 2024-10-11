from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import mealSerializer
from .models import meals
# Create your views here.
@api_view(['GET'])
def home(request,name):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=%s'
    response = requests.get(url)
    raw = response.json()
    data = raw['meals']
    categoryName = name
    # print(categoryName)
    filtered_meals = []
    for i in data:
      if i["strCategory"] == categoryName:
        data_db={
          "mealId" : i["idMeal"],
          "name" : i["strMeal"],
          "category" : i["strCategory"],
          "area" : i["strArea"],
          "liked": False 
        }
        serializer = mealSerializer(data = data_db)
        # print(serializer.data)
        if serializer.is_valid():
          if not meals.objects.filter(mealId=data_db["mealId"]).exists():
            serializer.save()
        filtered_meals.append(i)
    # print(filtered_meals[0])
    return Response({"meals":filtered_meals})
@api_view(['POST'])
def favourite(request,id):
  pass