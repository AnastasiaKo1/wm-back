from rest_framework import serializers
from api.models import Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id', 'name'

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    category = CategorySerializer()
    image = serializers.CharField()
    text = serializers.CharField()

    