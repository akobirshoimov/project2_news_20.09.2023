from django.shortcuts import render,get_object_or_404
from .models import NewsModel
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ListNewsView(APIView):
    def get(self,request):
        if str(request.user) != 'AnonymousUser':
            
            all = NewsModel.objects.all()
            serializer = NewsSerializer(all,many=True)
            return Response(serializer.data)
        return Response({'you can not read all info'})
    
class CreateNewsView(APIView):
    def post(self,request):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                serializer = NewsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else: 
                return Response({'you cannot add info only staff can add'})
        else:
             return Response({'you cannot add info only staff can add'})
        
    
class UpdateNewsView(APIView):
    def patch(self,request,*args,**kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:
                info = get_object_or_404(NewsModel,id=kwargs=['news_id'])
                serializer = NewsSerializer(info,data=request.data,partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'only admin can update '})
        return Response({'only admin can update '})
    
    
    
    
