from django.shortcuts import render

from api.models import Category, Article
from api.serializers import CategorySerializer, ArticleSerializer

from django.http.response import JsonResponse
from rest_framework.views import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

class Articles(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return JsonResponse(ArticleSerializer(articles, many=True).data, safe=False)

@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    return JsonResponse(CategorySerializer(categories, many=True).data, safe=False)
