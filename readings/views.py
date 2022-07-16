from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
import json
from minesafety.settings import BASE_DIR
from readings.models import ReadingData
from readings.serializers import ReadingDataSerializer

# class ReadingData(APIView):
#     def get(self, request, *args, **kwargs):
#         message = 'hi there'
#         return Response(message)

#     def post(self, request, *args, **kwargs):
#         message = '201 - created'
#         data = request.data
#         dstring = json.dumps(data)

#         pathfile = BASE_DIR / 'readingdata/api_data.txt'


#         with open(pathfile, 'w+') as f:

#             f.write(dstring)
#             print("File written successfully")
#         # close the file
#         f.close()
#         return Response(message)



class ReadingDataViewSet(viewsets.ModelViewSet):
    queryset = ReadingData.objects.all().order_by('-created')
    serializer_class = ReadingDataSerializer
    permission_classes = []
