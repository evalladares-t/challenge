#
from rest_framework import serializers
#
from applications.deliverables.models import Deliverable

class DeliverableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deliverable
        fields = ('id', 'name')