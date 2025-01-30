from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer

# Create your views here.
@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(serializer.data)

@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)