# imports
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions
from rest_framework import status

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        todos = ToDo.objects.filter(user = request.user.id)
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        
        
        data = {
            "task": request.data.get("task"),
            "completed": request.data.get("completed"),
            "user": request.user.id
        }
        
        
        serializer = ToDoSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)