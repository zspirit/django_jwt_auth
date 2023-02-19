from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
            {'GET': 'api/projects'},
            {'POST': 'api/users/token'}
            ]
    return Response(routes)
# serialize the object --> projects
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serialize = ProjectSerializer(projects, many=True)
    return Response(serialize.data)
'''
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    return Response(projects)'''