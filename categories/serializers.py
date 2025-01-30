from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = ('pk', 'name', 'kind', 'created_at')
