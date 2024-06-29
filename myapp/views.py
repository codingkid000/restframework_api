from django.shortcuts import render
from myapp.serializers import *
from myapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class DetailTable(APIView):
    def get(self,request):
        detailObj=DetailsModel.objects.all()
        delserializer=DetailSerializer(detailObj,many=True)
        return Response(delserializer.data)
    
    def post(self,request):
        serializersobj=DetailSerializer(data=request.data)
        if serializersobj.is_valid():
            serializersobj.save()
            return Response(200)
        return Response(serializersobj.errors)

class DetailsUpdate(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("not found in database")
        serializersobj=DetailSerializer(detailObj,data=request.data)
        if serializersobj.is_valid():
            serializersobj.save()
            return Response(200)
        return Response(serializersobj.errors)

class DetailsDelete(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("not found in database")
        serializersobj=DetailSerializer(detailObj,data=request.data)
        if serializersobj.is_valid():  
            serializersobj.save()
            return Response(200)
        return Response(serializersobj.errors)

