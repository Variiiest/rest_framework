from django.http import Http404
from rest_framework.response import Response 
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
#class_based_views
from rest_framework import permissions

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets , or create a new snippet
    """
    
    queryset= Snippet.objects.all()
    serializer_class= SnippetSerializer
    


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance
    """
    
    queryset= Snippet.objects.all()
    serializer_class= SnippetSerializer
    
    
    
class UserList(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    
    
  
    
    
    
    
    
    
    
    
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    
    # def put(self,request, *args , **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def delete(self,request, *args , **kwargs):
    #     return self.delete(request, *args, **kwargs)
    
    
    
    # def get_object(self, pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
        
    # def get(self, request, pk, format=None):
    #     snippet= self.get_object(pk)
    #     serializer= SnippetSerializer(snippet)
    #     return Response(serializer.data)
    
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk, format= None):
    #     snippet- self.get_object(pk)
    #     snippet.delete()
    #     return  Response(status= status.HTTP_204_NO_CONTENT)   





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
    
    

