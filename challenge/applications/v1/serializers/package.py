#
from rest_framework import serializers
#
from applications.packages.models import Package
from applications.deliverables.models import Deliverable
from applications.v1.serializers.deliverable import DeliverableSerializer

class PackageListSerializer(serializers.ModelSerializer):
    
    deliverables = serializers.SerializerMethodField(read_only=True)
    typeOfServiceID = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Package
        fields = ('id', 'description', 'price', 'typeOfServiceID', 'deliverables')

    def get_deliverables(self, package):
        data= Deliverable.objects.filter(package = package)
        return DeliverableSerializer(data, many= True).data

    def get_typeOfServiceID(self, package):
        return package.service.id

class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ('__all__')