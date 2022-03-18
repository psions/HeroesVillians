from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from .models import Supers



@api_view(['GET'])
def supers_list(request):
    supers = supers.objects.all()

    serializer = SuperSerializer(supers, many=True)

    
    return Response(serializer.data)
