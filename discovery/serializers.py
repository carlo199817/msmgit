from rest_framework import serializers
from .models import Store,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class StoreSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True, required=False)
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Store
        fields = ['id', 'store', 'date_posted', 'author', 'image', 'latitude','longitude','timenow','datenow']

    def validate(self, attrs):
        store = attrs.get('store', '')
        image = attrs.get('image', '')

        if not (store or image):
            raise serializers.ValidationError(
                self.default_error_messages
            )
        return attrs
