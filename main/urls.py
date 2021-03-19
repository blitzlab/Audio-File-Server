from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'main'
# Create a router and register our viewsets with it.

urlpatterns = [
    path('list-create/<str:audioFileType>', views.ListCreateView.as_view()), # Create one/List all files based on specified type
    path('<str:audioFileType>/<int:audioFileID>', views.RetrieveAudioView.as_view()), # Retreive file based on specified type and id
    path('<str:audioFileType>/<int:audioFileID>', views.UpdateAudioView.as_view()), # Update file based on specified type and id
    path('<str:audioFileType>/<int:audioFileID>', views.DeleteAudioView.as_view()), # Delete file based on specified type and id
]