
from applications.packages.models import Package
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from applications.v1.serializers.package import PackageListSerializer, PackageSerializer

class PackageList(APIView):

    serializer_class = PackageListSerializer

    def get (self,request,*args,**kwargs):
        serializer = self.serializer_class(Package.objects.all(), many=True)

        return Response(serializer.data)

class PackageResume(APIView):

    serializer_class = PackageSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Package,
                                 id=id)

    def get(self, request, *args, **kwargs):
        serializer = PackageListSerializer(
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