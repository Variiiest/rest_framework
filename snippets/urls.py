from django.urls import path
from .import views
urlpatterns = [
    path('list',views.snippet_list, name='snip_list' ),
]
