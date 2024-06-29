from rest_framework import serializers
from  myapp.models import *


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailsModel
        fields = "__all__"