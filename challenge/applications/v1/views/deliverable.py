from applications.deliverables.models import Deliverable
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.v1.serializers.deliverable import DeliverableSerializer

# Create your views here.

class DeliverableList(APIView):

    serializer_class = DeliverableSerializer

    def get (self,request,*args,**kwargs):
        serializer = self.serializer_class(Deliverable.objects.all(), many=True)

        return Response(serializer.data)

class DeliverableResume(APIView):

    serializer_class = DeliverableSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Deliverable,
                                 id=id)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.get_object())
        
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
                'success': True,
            },
                status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST)