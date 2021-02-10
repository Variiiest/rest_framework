from django.http import Http404
from rest_framework.response import Response 
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status


#class_based_views
class SnippetList(APIView):
    """
    List all snippets , or create a new snippet
    """
    
    def get(self, request, format= None):
        snippets= Snippet.objects.all()
        serializer= SnippetSerializer(snippets, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format= None):
        serializer= SnippetSerializer(snippets, many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class SnippetDetail(APIView):
    """
    """
    





# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     Listing all code snippets , or create a new snippet.
#     """
    
#     if request.method== 'GET':
#         snippets= Snippet.objects.all()
#         serializer= SnippetSerializer(snippets, many= True)
#         return JsonResponse(serializer.data, safe= False)
    
#     elif request.method=='POST':
#         data= JSONParser().parse(request)
#         serializer= SnippetSerializer(data= data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status= status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE']) 
# def snippet_detail(request, pk):
#     """
#     Retrieve , update or delete a code snippet.
#     """
#     try:
#         snippet= Snippet.objects.get(pk=pk)
        
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=400)
    
#     if request.method== 'GET':
#         serializer= SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#     elif request.method== 'PUT':
#         data= JSONParser().parse(request)
#         serializer= SnippetSerializer(snippet, data= data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method== 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    

