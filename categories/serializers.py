from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=150)
    kind = serializers.ChoiceField(choices=Category.CategoriesKindChoices.choices)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = ('pk', 'name', 'kind', 'created_at')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)