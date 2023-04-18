from rest_framework import serializers

from api.models import Member, Service


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["pk", "name", "description", "service"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["pk", "name", "description", "photo"]
