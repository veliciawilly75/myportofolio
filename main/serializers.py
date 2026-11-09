from django.utils.html import strip_tags
from rest_framework import serializers

from .models import Projects, Experience, Skill

class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    is_solo = serializers.ReadOnlyField()
    link_available = serializers.ReadOnlyField()

    class Meta:
        model = Projects
        fields = [
            "id", "title", "description",
            "status", "type", "link",
            "star_count", "is_starred", "starred_by_names",
            "is_solo", "link_available",
        ]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names", "is_solo", "link_available"] 

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    is_ongoing = serializers.ReadOnlyField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description",
            "category", "started_at", "ended_at",
            "star_count", "is_starred", "starred_by_names",
            "is_ongoing",
        ]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names", "is_ongoing"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value
    
    def validate_description(self, value):
        return strip_tags(value)

    def validate(self, data):
        started_at = data.get('started_at', getattr(self.instance, 'started_at', None))
        ended_at = data.get('ended_at', getattr(self.instance, 'ended_at', None))
        if ended_at != None and ended_at <= started_at:
            raise serializers.ValidationError("End datetime must be after Start datetime.")
        return data

    def get_star_count(self, obj):
        return obj.starred_by.count()
    
    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()
    
    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

    def to_internal_value(self, data):
        # Frontend FormData is often immutable, so we make a mutable copy
        mutable_data = data.copy()
        
        # If the frontend sent an empty string, convert it to None
        if mutable_data.get('ended_at') == '':
            mutable_data['ended_at'] = None
            
        return super().to_internal_value(mutable_data)

class SkillSerializer(serializers.ModelSerializer):
    prioritize = serializers.ReadOnlyField()
    highlight = serializers.ReadOnlyField()
    certif_available = serializers.ReadOnlyField()

    class Meta:
        model = Skill
        fields = [
            "id", "title", "level", "certification",
            "prioritize", "highlight", "certif_available",
        ]
        read_only_fields = ["id", "prioritize", "highlight", "certif_available"] 

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def to_internal_value(self, data):
        # Frontend FormData is often immutable, so we make a mutable copy
        mutable_data = data.copy()
            
        # If the frontend sent an empty string, convert it to None
        if mutable_data.get('certification') == '':
            mutable_data['certification'] = None
                
        return super().to_internal_value(mutable_data)