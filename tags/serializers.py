from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color', 'created_at']
        read_only_fields = ['id', 'created_at']
        ref_name = 'TagSerializer'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Tag name too short")
        return value

    def validate_color(self, value):
        if not value.startswith('#') or len(value) not in [4, 7]:
            raise serializers.ValidationError("Color must be in hex format (e.g. #RRGGBB or #RGB)")
        return value