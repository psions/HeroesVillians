from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from .models import super



@api_view(['GET'])
def supers_list(request):
    supers = super.objects.all()

    serializer = SuperSerializer(supers, many=True)

    
    return Response(serializer.data)
