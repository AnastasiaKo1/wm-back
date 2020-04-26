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

@api_view(['POST'])
def create_article(request):
    try:
        category = Category.objects.get(name=request.data.get('category'))
    except:
        category = Category.objects.create(name=request.data.get('category'))
        
    article = Article.objects.create(
        category = category,
        title = request.data.get('title'),
        image = request.data.get('image'),
        text = request.data.get('text')
    )
    return JsonResponse(ArticleSerializer(article).data, safe=False)

