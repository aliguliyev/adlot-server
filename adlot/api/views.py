from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from platformdirs import api
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list' : '/task-list',
        'Detail View' : '/task-detail/<str:pk>',
        'Create' : '/task-create',
        'Update' : 'task-update/<str:pk>',
        'Delete' : 'task-delete/<str:pk>',
    }
    return Response(api_urls)