from .models import Song, Podcast, Audiobook
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from config.constants import audioFileType
# Create your views here.

class ListCreateView(generics.ListCreateAPIView):
    serializer_class = SongSerializer


class RetrieveAudioView(generics.RetrieveAPIView):
    pass

class UpdateAudioView(generics.UpdateAPIView):
    pass

class DeleteAudioView(generics.DestroyAPIView):
    pass

class ListAudioView(generics.ListAPIView):
    serializer_class = SongSerializer

    queryset = Song.objects.all()





 # def post(self, request, *args, **kwargs):
    #     if (not request.data.get("audioFileType")):
    #         print("audioFileType has no value") 
        #     request.data["first_name"] = name
        #     request.data["last_name"] = surname
        #     return self.create(request, *args, **kwargs)
        # return self.create(request, *args, **kwargs)
        # print(file_type in audioFileType)