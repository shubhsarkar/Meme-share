from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meme
from .serializers import MemeSerializer

# Create your views here.

def home(request):
    return render(request,"index.html")

def submit(request):
    entry_owner = request.POST["form-name"]
    entry_cap = request.POST["form-caption"]
    entry_url = request.POST["form-url"]

    entry_info = Meme(owner=entry_owner, url=entry_url, cap=entry_cap)
    
    entry_info.save()

    memes = Meme.objects.all()

    return render(request, "show.html", {"memes": memes})

def memeList(request):
    if request.method == "GET":
        memes = Meme.objects.all()
        serializer = MemeSerializer(memes,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MemeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)