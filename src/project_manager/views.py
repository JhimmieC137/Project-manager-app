from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings

from .models import Project
from .serializers import ProjectSerializer

class ProjectsViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [
        # IsAdminUser
    ]
    queryset = Project.objects.all()
    
    def get_queryset(self):                                      
        return super().get_queryset()
    
    serializers = {
        'default': ProjectSerializer, 
        'create': ProjectSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])
    
    #Create mixin methods
    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}
    
    def perform_create(self, serializer):
        serializer.save()
    
    def create(self, request):  
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response("400 BAD REQUEST", status=status.HTTP_400_BAD_REQUEST)
        
    #Update mixin methods
    def perform_update(self, serializer):
        serializer.save()
        
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        try:
            return self.update(request, *args, **kwargs)
        except:
            return Response("400 BAD REQUEST", status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_update(serializer)
            return Response(serializer.data)
        
        except:
            return Response("400 BAD REQUEST", status=status.HTTP_400_BAD_REQUEST)
