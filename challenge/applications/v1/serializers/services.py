#
from rest_framework import serializers
#
from applications.services.models import Service
from applications.packages.models import Package
from applications.v1.serializers.package import PackageSerializer, PackageListSerializer

class ServiceListSerializer(serializers.ModelSerializer):

    packages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'packages')

    def get_packages(self, service):
        data= Package.objects.filter(service = service)
        return PackageListSerializer(data, many= True).data

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = ('__all__')