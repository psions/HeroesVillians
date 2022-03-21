from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuperSerializer
from .models import Supers




@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':

        hero_name = request.query_params.get('super_type_id')
        print(hero_name)

        queryset = Supers.objects.all()

        if hero_name:
            queryset=queryset.filter(hero__name = hero_name)



        supers = Supers.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == "GET":
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

  
   