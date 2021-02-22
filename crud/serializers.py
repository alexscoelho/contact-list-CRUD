from rest_framework import serializers
from crud.models import Contact, Group


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email', 'address', 'phone')
        # extra_kwargs = {'groups': {'required': False}}

class GroupSerializer(serializers.ModelSerializer):
    contacts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id','name', 'created_at', 'contacts')
        # extra_kwargs = {'contacts': {'required': False}}