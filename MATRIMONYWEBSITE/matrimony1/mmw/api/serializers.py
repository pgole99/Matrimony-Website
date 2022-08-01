from mmw.models import personinfo
from rest_framework import serializers

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=personinfo
        fields=['name','email','gender','date','religion','city','age','physical_disability','education','occupation','img','biodata']